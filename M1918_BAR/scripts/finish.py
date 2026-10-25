"""Final finish with ffmpeg (no DaVinci): 1080p60 picture from timeline rows, VO + music bed (ducked) + MG SFX, 5 s outro, -14 LUFS. Usage: finish.py segs|music|final"""
import json,subprocess,os,sys
from concurrent.futures import ThreadPoolExecutor
B='/tmp/claude-0/bar'; F=f'{B}/final'; TL=json.load(open(f'{B}/voice/timeline.json')); T=TL['total']
SRC={'V01':f'{B}/vid/v1925.mp4','V02':f'{B}/master/ADC-3426c.mov','V03':f'{B}/vid/FuryInThePacific.mp4','V04':f'{B}/master/gov.dod.dimoc.20276.mpeg',
 'V05':f'{B}/master/H-1423.mov','V06':f'{B}/master/NPC-11271.mov','V07':f'{B}/master/gov.dod.dimoc.20377.mpeg','V08':f'{B}/master/ADC-3960c.mov',
 'V09':f'{B}/vid/MCSO.mp4','V10':f'{B}/vid/CB108.mp4'}
INTERLACED={'V04','V07'}
PH={'P01':'P_val.jpg','P02':'P_325.jpg','P03':'P_cape.jpg','P04':'Marine_BAR_shooting_NA01862.jpg','P05':'P_zajas.jpg','P06':'P_m27.jpg'}
FIT="scale=1920:1080:force_original_aspect_ratio=decrease:flags=lanczos,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=60,format=yuv420p"
ENC=['-c:v','libx264','-preset','medium','-crf','16','-an']
def run(c): subprocess.run(['ffmpeg','-y','-loglevel','error']+c,check=True)
def seg(r):
    o=f"{F}/seg/{r['n']:03d}.mp4"; d=r['dur']
    if os.path.exists(o): return
    if r['kind']=='V':
        vf=('yadif=0,' if r['code'] in INTERLACED else '')+FIT
        run(['-ss',str(r['src_in']),'-i',SRC[r['code']],'-t',f'{d:.3f}','-vf',vf]+ENC+[o])
    elif r['kind']=='P':
        st=f"{B}/rc/still/{r['code']}.png"; n=int(round(d*60))
        run(['-loop','1','-i',st,'-vf',f"zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=60,format=yuv420p",'-frames:v',str(n)]+ENC+[o])
    else:
        run(['-i',f"{B}/mg/{r['code']}/{r['code']}_out.mp4",'-t',f'{d:.3f}','-vf','setsar=1,fps=60,format=yuv420p']+ENC+[o])
mode=sys.argv[1]
if mode=='segs':
    with ThreadPoolExecutor(2) as ex: list(ex.map(seg,TL['rows']))
    print('segs ok')
# music plan: (start_s, end_s, file, source_offset_s)
off=TL['vo_offsets']
PLAN=[(0,off['VO03'],'black-vortex-by-kevin-macleod.mp3',0),
      (off['VO03'],off['VO05'],'greenland-by-alex-productions.mp3',0),
      (off['VO05'],off['VO07'],'exalted-by-aylex.mp3',0),
      (off['VO07'],off['VO08'],'black-vortex-by-kevin-macleod.mp3',40),
      (off['VO08'],T,'greenland-by-alex-productions.mp3',95)]
XF=3.0
if mode=='music':
    parts=[]
    for k,(a,b,f,so) in enumerate(PLAN):
        L=b-a+(XF if k<len(PLAN)-1 else 0); o=f'{F}/music/part{k}.wav'
        fin=0 if k==0 else XF
        run(['-ss',str(so),'-i',f'{F}/music/{f}','-t',f'{L:.3f}','-af',f'loudnorm=I=-16:TP=-2,afade=t=in:d={max(fin,0.01)},afade=t=out:st={L-XF:.3f}:d={XF}','-ar','48000','-ac','2',o])
        parts.append((a,o))
    ins=[];flt=[]
    for k,(a,o) in enumerate(parts):
        ins+=['-i',o]; ms=int(a*1000); flt.append(f'[{k}]adelay={ms}|{ms}[m{k}]')
    flt.append(''.join(f'[m{k}]' for k in range(len(parts)))+f'amix=inputs={len(parts)}:normalize=0,atrim=0:{T:.3f}[m]')
    run(ins+['-filter_complex',';'.join(flt),'-map','[m]','-ar','48000',f'{F}/music_bed.wav'])
    print('music ok')
if mode=='final':
    rows=TL['rows']
    with open(f'{F}/list.txt','w') as fl:
        for r in rows: fl.write(f"file '{F}/seg/{r['n']:03d}.mp4'\n")
    run(['-f','concat','-safe','0','-i',f'{F}/list.txt','-c','copy',f'{F}/video_only.mp4'])
    ins=['-i',f'{F}/video_only.mp4','-i',f'{F}/music_bed.wav']; flt=[]
    vos=sorted(off.items())
    for k,(v,o) in enumerate(vos):
        ins+=['-i',f'{B}/voice/{v}.mp3']; ms=int(o*1000); flt.append(f'[{k+2}]aresample=48000,adelay={ms}|{ms}[v{k}]')
    nv=len(vos); g=[r for r in rows if r['kind']=='G']
    for j,r in enumerate(g):
        ins+=['-i',f"{B}/mg/{r['code']}/{r['code']}_sfx.wav"]; ms=int(r['start']*1000); flt.append(f'[{nv+2+j}]atrim=0:{r["dur"]:.3f},adelay={ms}|{ms}[s{j}]')
    flt.append(''.join(f'[v{k}]' for k in range(nv))+f'amix=inputs={nv}:normalize=0,volume=11dB,apad,atrim=0:{T:.3f},asplit=2[vo][sc]')
    E0=TL['narration_end']
    # bed level: -16 LUFS track normalised, then -10 dB -> ~-26 LUFS; duck ~4 dB under speech; slight outro swell then fade
    flt.append(f"[1]volume=-10dB,volume='if(gt(t,{E0:.2f}),1+0.5*min(1,(t-{E0:.2f})/1.5),1)':eval=frame,afade=t=out:st={T-3.5:.3f}:d=3.5[bed]")
    flt.append('[bed][sc]sidechaincompress=threshold=0.03:ratio=3:attack=300:release=600:makeup=1[duck]')
    flt.append('[vo][duck]'+''.join(f'[s{j}]' for j in range(len(g)))+f'amix=inputs={2+len(g)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]')
    flt.append(f'[0:v]fade=t=out:st={T-3.0:.3f}:d=3.0[vid]')
    run(ins+['-filter_complex',';'.join(flt),'-map','[vid]','-map','[a]','-t',f'{T:.3f}','-c:v','libx264','-preset','medium','-b:v','20M','-maxrate','24M','-bufsize','40M','-profile:v','high','-pix_fmt','yuv420p','-r','60','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart',f'{F}/M1918_BAR_final.mp4'])
    print('final ok')
