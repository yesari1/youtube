"""Rough-cut preview: 1280x720 30fps segments per timeline row, concat, VO mix, outro fade. Usage: roughcut.py [segs|G|final]"""
import json,subprocess,os,sys
from concurrent.futures import ThreadPoolExecutor
B='/tmp/claude-0/bar'; RC=f'{B}/rc'; TL=json.load(open(f'{B}/voice/timeline.json'))
SRC={'V01':f'{B}/vid/v1925.mp4','V02':f'{B}/master/ADC-3426c.mov','V03':f'{B}/vid/FuryInThePacific.mp4','V04':f'{B}/master/gov.dod.dimoc.20276.mpeg',
 'V05':f'{B}/master/H-1423.mov','V06':f'{B}/master/NPC-11271.mov','V07':f'{B}/vid/gov.dod.dimoc.20377_512kb.mp4','V08':f'{B}/master/ADC-3960c.mov',
 'V09':f'{B}/vid/MCSO.mp4','V10':f'{B}/vid/CB108.mp4'}
PH={'P01':'P_val.jpg','P02':'P_325.jpg','P03':'P_cape.jpg','P04':'Marine_BAR_shooting_NA01862.jpg','P05':'P_zajas.jpg','P06':'P_m27.jpg'}
GF={'G01':'G01','G02':'G02','G03':'G03','G04':'G04','G05':'G05','G06':'G06'}
FIT="scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,format=yuv420p"
ENC=['-c:v','libx264','-preset','veryfast','-crf','21','-an']
def run(c): subprocess.run(['ffmpeg','-y','-loglevel','error']+c,check=True)
def seg(r):
    o=f"{RC}/seg/{r['n']:03d}.mp4"; d=r['dur']
    if r['kind']=='V':
        run(['-ss',str(r['src_in']),'-i',SRC[r['code']],'-t',f'{d:.3f}','-vf',FIT]+ENC+[o])
    elif r['kind']=='P':
        st=f"{RC}/still/{r['code']}.png"
        if not os.path.exists(st):
            run(['-i',f"{B}/photos/{PH[r['code']]}",'-filter_complex',
              "[0]scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,gblur=sigma=40,eq=brightness=-0.12[bg];[0]scale=3840:2160:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2",'-frames:v','1',st])
        n=int(round(d*30))
        run(['-loop','1','-i',st,'-vf',f"zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=30,format=yuv420p",'-frames:v',str(n)]+ENC+[o])
    elif r['kind']=='G':
        run(['-i',f"{B}/mg/{r['code']}/{r['code']}_out.mp4",'-t',f'{d:.3f}','-vf',FIT]+ENC+[o])
    return o
mode=sys.argv[1]
rows=TL['rows']
if mode in('segs','G'):
    todo=[r for r in rows if (r['kind']=='G')==(mode=='G')]
    with ThreadPoolExecutor(2) as ex: list(ex.map(seg,todo))
    print('segs done',len(todo))
if mode=='final':
    with open(f'{RC}/list.txt','w') as f:
        for r in rows: f.write(f"file '{RC}/seg/{r['n']:03d}.mp4'\n")
    run(['-f','concat','-safe','0','-i',f'{RC}/list.txt','-c','copy',f'{RC}/video_only.mp4'])
    T=TL['total']; ins=[]; flt=[]
    for k,(v,off) in enumerate(sorted(TL['vo_offsets'].items())):
        ins+=['-i',f'{B}/voice/{v}.mp3']; ms=int(off*1000); flt.append(f'[{k+1}]adelay={ms}|{ms}[a{k}]')
    nv=len(TL['vo_offsets'])
    flt.append(''.join(f'[a{k}]' for k in range(nv))+f'amix=inputs={nv}:normalize=0,apad,atrim=0:{T:.3f}[vo]')
    flt.append(f"[0:v]fade=t=out:st={T-3.0:.3f}:d=3.0[v]")
    run(['-i',f'{RC}/video_only.mp4']+ins+['-filter_complex',';'.join(flt),'-map','[v]','-map','[vo]','-t',f'{T:.3f}','-c:v','libx264','-preset','veryfast','-crf','22','-c:a','aac','-b:a','192k','-movflags','+faststart',f'{RC}/M1918_BAR_rough_cut_preview.mp4'])
    print('final done')
