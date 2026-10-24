import json,re,sys,difflib
sys.path.insert(0,'/tmp/claude-0/bar/pkg'); import importlib.util
spec=importlib.util.spec_from_file_location('rows','/tmp/claude-0/bar/pkg/rows.py'); rows=importlib.util.module_from_spec(spec); spec.loader.exec_module(rows)
W=json.load(open('/tmp/claude-0/bar/voice/words.json'))
num={'0':'zero'}
def norm(s):
    s=re.sub(r'\[[^\]]*\]','',s).lower().replace('-',' ').replace('—',' ')
    return [w for w in re.sub(r"[^a-z0-9' ]",' ',s).split() if w]
out=[]
for vo in sorted(W):
    ws=W[vo]; asr=[norm(w[0]) for w in ws]
    flat=[];idx=[]
    for i,a in enumerate(asr):
        for x in a: flat.append(x); idx.append(i)
    rr=[r for r in rows.R if r['vo']==vo]
    toks=[];own=[]
    for j,r in enumerate(rr):
        for x in norm(r['text']): toks.append(x); own.append(j)
    sm=difflib.SequenceMatcher(None,toks,flat,autojunk=False)
    m={}
    for a,b,n in sm.get_matching_blocks():
        for k in range(n): m[a+k]=b+k
    starts=[]
    for j in range(len(rr)):
        ks=[k for k in range(len(toks)) if own[k]==j]
        hit=[(k,m[k]) for k in ks if k in m]
        if not hit: starts.append(None); continue
        k0,b0=hit[0]; ws_i=idx[b0]
        # back off by number of unmatched leading tokens (approx 0.3 s each)
        starts.append(max(0,ws[ws_i][1]-0.3*(k0-ks[0])))
    ends=[]
    for j,r in enumerate(rr):
        ks=[k for k in range(len(toks)) if own[k]==j]; hit=[m[k] for k in ks if k in m]
        ends.append(ws[idx[hit[-1]]][2] if hit else None)
    for j,r in enumerate(rr):
        out.append(dict(vo=vo,i=j,kind=r['kind'],code=r['code'],s=starts[j],e=ends[j],plan=r.get('d') or (r.get('b',0)-r.get('a',0)),text=r['text'][:60]))
json.dump(out,open('/tmp/claude-0/bar/voice/rowtimes.json','w'),indent=0)
for o in out: print(o['vo'],o['i'],o['kind'],o['code'],o['s'] and round(o['s'],2),o['e'] and round(o['e'],2),round(o['plan'],1),o['text'][:40])
