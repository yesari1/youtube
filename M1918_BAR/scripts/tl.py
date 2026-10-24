import json,csv,importlib.util,subprocess
spec=importlib.util.spec_from_file_location('rows','/tmp/claude-0/bar/pkg/rows.py'); rows=importlib.util.module_from_spec(spec); spec.loader.exec_module(rows)
RT=json.load(open('/tmp/claude-0/bar/voice/rowtimes.json'))
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
GAP=0.8; OUTRO=5.0
vos=sorted({r['vo'] for r in RT}); L={v:dur(f'/tmp/claude-0/bar/voice/{v}.mp3') for v in vos}
off={};t=0
for v in vos: off[v]=t; t+=L[v]+GAP
END=off[vos[-1]]+L[vos[-1]]
TOTAL=END+OUTRO
rr=[r for r in rows.R]
out=[]
for k,(r,o) in enumerate(zip(rr,RT)):
    s=off[o['vo']]+(0 if o['i']==0 else o['s'])
    if k+1<len(RT): nxt=RT[k+1]; e=off[nxt['vo']]+(0 if nxt['i']==0 else nxt['s'])
    else: e=TOTAL
    d=e-s; row=dict(n=k+1,chapter=r['ch'],vo=o['vo'],kind=r['kind'],code=r['code'],start=round(s,3),end=round(e,3),dur=round(d,3))
    if r['kind']=='V':
        row['src_in']=round(r['a'],3); row['src_out']=round(r['a']+d,3); row['planned_src_out']=round(r['b'],3)
    row['desc']=r['desc']; row['text']=r['text']; out.append(row)
json.dump(dict(vo_offsets=off,vo_len=L,narration_end=END,total=TOTAL,rows=out),open('/tmp/claude-0/bar/voice/timeline.json','w'),indent=1)
def tc(x): return f"{int(x//60)}:{x%60:04.1f}"
print('TOTAL',tc(TOTAL),'narr end',tc(END))
for v in vos: print(v,tc(off[v]),round(L[v],1))
for r in out:
    if r['kind']!='V' or r['dur']>(r.get('planned_src_out',0)-r.get('src_in',0))+0.5: print(r['n'],r['kind'],r['code'],tc(r['start']),round(r['dur'],1))
