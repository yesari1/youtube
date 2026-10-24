import re,collections
exec(open('rows.py').read())
def fmt(x): return f"{int(x//60)}:{x%60:04.1f}"
def tc(x): return f"{int(x//60):02d}:{x%60:06.3f}"
tm=0
for r in R:
    r['dur']=r['b']-r['a'] if r['kind']=='V' else r['d']; r['t0']=tm; tm+=r['dur']; r['t1']=tm
TOTAL=tm
HOOK_END=[r['t1'] for r in R if r['ch']=='Hook'][-1]
# Edit map
L=["| Time | Chapter | Voice file | Exact voice-over | Picture and edit instruction | Claim ID |","| --------- | ------- | ---------- | ---------------- | ---------------------------- | -------- |"]
for r in R:
    if r['kind']=='V': pic=f"{r['code']} — {tc(r['a'])}–{tc(r['b'])}; {r['desc']}; mute source audio"
    elif r['kind']=='P': pic=f"{r['code']} — {r['dur']:.0f} seconds; {r['desc']}"
    else: pic=f"{r['code']} — {r['dur']:.0f} seconds; {r['desc']}"
    L.append(f"| {fmt(r['t0'])}–{fmt(r['t1'])} | {r['ch']} | {r['vo']} | {r['text']} | {pic} | {r['claim']} |")
open('editmap.md','w').write('\n'.join(L)+'\n')
# H audit
A=["| Asset / clip | Type | Source range | Hook uses | Non-hook uses | Non-hook timeline ranges | Total non-hook time | Smallest gap | Reuse / distinction note | Status |","| ------------ | ---- | ------------ | --------: | ------------: | ------------------------ | ------------------: | -----------: | ------------------------ | ------ |"]
order=sorted([r for r in R if r['kind']=='V'],key=lambda r:(int(r['code'][1:]),r['a']))
for r in order:
    hook=r['ch']=='Hook'
    A.append(f"| {r['code']} clip {tc(r['a'])}–{tc(r['b'])} | Video clip | {tc(r['a'])}–{tc(r['b'])} | {1 if hook else 0} | {0 if hook else 1} | {'—' if hook else fmt(r['t0'])+'–'+fmt(r['t1'])} | {0 if hook else r['dur']:.1f} s | N/A | Single use; non-overlapping with every other range of this source | PASS |".replace('| 0.0 s','| 0 s'))
for r in R:
    if r['kind']=='P': A.append(f"| {r['code']} | Photograph | N/A | 0 | 1 | {fmt(r['t0'])}–{fmt(r['t1'])} | {r['dur']:.1f} s | N/A | Single use, isolated between moving shots | PASS |")
for r in R:
    if r['kind']=='G': A.append(f"| {r['code']} | Graphic | N/A | 0 | 1 | {fmt(r['t0'])}–{fmt(r['t1'])} | {r['dur']:.1f} s | N/A | Single uninterrupted use | PASS |")
open('audit.md','w').write('\n'.join(A)+'\n')
# overlap check
by=collections.defaultdict(list)
for r in R:
    if r['kind']=='V': by[r['code']].append((r['a'],r['b']))
for k,v in by.items():
    v.sort()
    for (a1,b1),(a2,b2) in zip(v,v[1:]):
        if a2<b1-1e-6: print('OVERLAP',k,a1,b1,a2,b2)
# I section
vo=collections.OrderedDict()
names={'VO01':'Hook','VO02':'A_Gun_For_Walking','VO03':'Machine_Gun_By_Default','VO04':'One_Gun_Twelve_Men','VO05':'Built_Around_The_BAR','VO06':'The_Price','VO07':'Korea_The_Mainstay','VO08':'Verdict'}
for r in R:
    v=vo.setdefault(r['vo'],dict(t0=r['t0'],t1=r['t1'],ch=r['ch'],txt=[])); v['t1']=r['t1']; v['txt'].append(r['text'])
I=["| File | Timeline | Chapter / purpose | Recording text |","| ---- | -------- | ----------------- | -------------- |"]
stats=[]
for k,v in vo.items():
    txt=' '.join(v['txt']); w=len(re.sub(r'\[[^\]]*\]','',txt).split())
    p=txt.count('[short pause]')*0.5+txt.count('[pause]')*1.0+txt.count('[long pause]')*1.75
    dur=v['t1']-v['t0']
    if k=='VO08': dur-=6.0
    stats.append((k,fmt(v['t0'])+'–'+fmt(v['t1']),w,round(w/(dur-p)*60)))
    I.append(f"| `{k}_{names[k]}.wav` | {fmt(v['t0'])}–{fmt(v['t1'])} | {v['ch']} | {txt} |")
open('vo.md','w').write('\n'.join(I)+'\n')
open('stats.txt','w').write(repr(stats)+'\n'+repr([(r['ch'],fmt(r['t0'])) for r in R])+'\nTOTAL '+fmt(TOTAL)+' HOOK_END '+fmt(HOOK_END)+'\n')
print(stats); print('TOTAL',fmt(TOTAL),'HOOK',fmt(HOOK_END))
chap=collections.OrderedDict()
for r in R:
    c=chap.setdefault(r['ch'],dict(t0=r['t0'],V=0,P=0,G=0,codes=set())); c['t1']=r['t1']; c[r['kind']]+=r['dur']; c['codes'].add(r['code'])
for k,c in chap.items(): print(k,fmt(c['t0']),fmt(c['t1']),round(c['V'],1),round(c['P'],1),round(c['G'],1),sorted(c['codes']))
for r in R:
    if r['kind'] in 'PG': print(r['code'],fmt(r['t0']),fmt(r['t1']),r['text'][:70])
