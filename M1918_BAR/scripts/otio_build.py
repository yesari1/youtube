"""rough_cut.otio + rough_cut_timeline.csv + rough_cut_manifest.json with PC target paths (D:\\Youtube\\Warfront Archives\\Titles\\M1918_BAR)."""
import json,csv,opentimelineio as otio,os
B='/tmp/claude-0/bar'; TL=json.load(open(f'{B}/voice/timeline.json')); OUT=f'{B}/deliver'; os.makedirs(OUT,exist_ok=True)
ROOT=r'D:\Youtube\Warfront Archives\Titles\M1918_BAR'
VEXT={'V01':'.mp4','V02':'.mov','V03':'.mp4','V04':'.mpeg','V05':'.mov','V06':'.mov','V07':'.mpeg','V08':'.mov','V09':'.mp4','V10':'.mp4'}
GN={'G01':'G01_Twenty_Rounds_Two_Seconds','G02':'G02_Two_Ways_to_Build_a_Squad','G03':'G03_What_the_BAR_Man_Carried','G04':'G04_What_Marshall_Found','G05':'G05_Three_Wars_of_Production','G06':'G06_Forty_Years_Three_Jobs'}
R=30
def rt(s): return otio.opentime.RationalTime(round(s*R),R)
def tr(a,d): return otio.opentime.TimeRange(rt(a),rt(d))
def path(r):
    k,c=r['kind'],r['code']
    if k=='V': return ROOT+rf'\Videos\{c}{VEXT[c]}'
    if k=='P': return ROOT+rf'\Photos\{c}.jpg'
    return ROOT+rf'\Graphics\Motion\{GN[c]}.mp4'
tl=otio.schema.Timeline(name='M1918_BAR_rough_cut',global_start_time=rt(0))
v=otio.schema.Track(name='V1 picture',kind=otio.schema.TrackKind.Video)
sfx=otio.schema.Track(name='A2 MG sfx',kind=otio.schema.TrackKind.Audio)
vo=otio.schema.Track(name='A1 voiceover',kind=otio.schema.TrackKind.Audio)
t_sfx=0
for r in TL['rows']:
    src=r.get('src_in',0) if r['kind']=='V' else 0
    v.append(otio.schema.Clip(name=f"{r['n']:03d} {r['code']}",media_reference=otio.schema.ExternalReference(target_url=path(r)),source_range=tr(src,r['dur']),metadata={'row':r['n'],'chapter':r['chapter'],'kind':r['kind']}))
    if r['kind']=='G':
        gap=r['start']-t_sfx
        if gap>0: sfx.append(otio.schema.Gap(source_range=tr(0,gap)))
        sfx.append(otio.schema.Clip(name=f"{r['code']}_sfx",media_reference=otio.schema.ExternalReference(target_url=ROOT+rf"\Graphics\Motion\{r['code']}_sfx.wav"),source_range=tr(0,r['dur'])))
        t_sfx=r['start']+r['dur']
t=0
for k,(name,off) in enumerate(sorted(TL['vo_offsets'].items())):
    if off-t>0: vo.append(otio.schema.Gap(source_range=tr(0,off-t)))
    L=TL['vo_len'][name]; vo.append(otio.schema.Clip(name=name,media_reference=otio.schema.ExternalReference(target_url=ROOT+rf'\Voice\{k+1}.mp3'),source_range=tr(0,L)))
    t=off+L
tl.tracks.extend([v,vo,sfx])
otio.adapters.write_to_file(tl,f'{OUT}/rough_cut.otio')
def tc(x): return f"{int(x//60)}:{x%60:06.3f}"
with open(f'{OUT}/rough_cut_timeline.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['row','chapter','voice_file','kind','code','start','end','duration_s','source_in','source_out','media_path','narration'])
    for r in TL['rows']:
        w.writerow([r['n'],r['chapter'],r['vo'],r['kind'],r['code'],tc(r['start']),tc(r['end']),f"{r['dur']:.3f}",tc(r['src_in']) if r['kind']=='V' else '',tc(r['src_out']) if r['kind']=='V' else '',path(r),r['text']])
man=dict(video='M1918 BAR (Warfront Archives)',total_s=round(TL['total'],3),narration_end_s=round(TL['narration_end'],3),outro_s=5.0,fps=30,
 voice=[dict(file=rf'Voice\{k+1}.mp3',section=n,offset_s=round(o,3),length_s=round(TL['vo_len'][n],3)) for k,(n,o) in enumerate(sorted(TL['vo_offsets'].items()))],
 graphics={c:dict(file=rf'Graphics\Motion\{GN[c]}.mp4',sfx=rf'Graphics\Motion\{c}_sfx.wav',fps=60,size='1920x1080') for c in GN},
 notes=['Row times come from faster-whisper word timestamps of the final ElevenLabs takes.','V source_out may run past the planned out-point by up to ~3 s where the narration ran longer than planned; check those cuts by eye.','No music in this rough cut; music is added in the DaVinci step.'])
json.dump(man,open(f'{OUT}/rough_cut_manifest.json','w'),indent=1,ensure_ascii=False)
print('ok',len(TL['rows']))
