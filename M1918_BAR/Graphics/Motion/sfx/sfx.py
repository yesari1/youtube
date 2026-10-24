"""Synthesised soft SFX for G01-G06 (procedural, no third-party samples -> no licence constraints). Output Gnn_sfx.wav 48k stereo, normalised to about -30 LUFS."""
import numpy as np, subprocess, sys
SR=48000; rng=np.random.default_rng(7)
def env(n,a,d): t=np.arange(n)/SR; return np.minimum(1,t/max(a,1e-4))*np.exp(-t/d)
def tick(f=2400,d=0.018,g=1.0):
    n=int(SR*0.12); t=np.arange(n)/SR; return g*np.sin(2*np.pi*f*t)*env(n,0.0008,d)+g*0.3*rng.standard_normal(n)*env(n,0.0005,d*0.4)
def thud(f=140,d=0.07,g=1.0):
    n=int(SR*0.4); t=np.arange(n)/SR; return g*np.sin(2*np.pi*(f*t-30*t*t))*env(n,0.002,d)+g*0.15*np.convolve(rng.standard_normal(n),np.ones(40)/40,'same')*env(n,0.001,d*0.5)
def chime(f=880,d=0.9,g=0.6):
    n=int(SR*2.5); t=np.arange(n)/SR; return g*(np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*2.01*f*t)+0.15*np.sin(2*np.pi*3.02*f*t))*env(n,0.004,d)
def whoosh(dur=0.9,g=0.6,lo=300,hi=2500):
    n=int(SR*dur); x=rng.standard_normal(n); X=np.fft.rfft(x); fr=np.fft.rfftfreq(n,1/SR)
    X*=np.exp(-((np.log(fr+1)-np.log((lo*hi)**.5))**2)/1.2); y=np.fft.irfft(X,n); w=np.sin(np.pi*np.arange(n)/n)**2; return g*y/np.abs(y).max()*w
def key(g=0.7):
    a=thud(f=320,d=0.02,g=0.4*g); b=tick(f=1800+rng.uniform(-200,200),d=0.012,g=g); a[:len(b)]+=b; return a
def swell(dur=1.6,f=110,g=0.5):
    n=int(SR*dur); t=np.arange(n)/SR; return g*(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*1.5*t))*np.sin(np.pi*t/dur)**2*0.6
def build(dur,events,name):
    out=np.zeros((int(SR*dur)+SR,2))
    for t0,snd,pan in events:
        i=int(t0*SR); s=snd[:len(out)-i]; l=np.cos((pan+1)*np.pi/4); r=np.sin((pan+1)*np.pi/4)
        out[i:i+len(s),0]+=s*l; out[i:i+len(s),1]+=s*r
    out=out[:int(SR*dur)]
    raw=f'/tmp/claude-0/bar/mg/sfx/{name}_raw.wav'
    import wave; w=wave.open(raw,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out/np.abs(out).max()*0.5*32767).astype('<i2').tobytes()); w.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',raw,'-af','loudnorm=I=-30:TP=-6:LRA=11','-ar','48000',f'/tmp/claude-0/bar/mg/{name[:3]}/{name}.wav'],check=True)
# G01: rounds leave the magazine at 550 rpm, stamp chime, lower-row soft ticks
burst=5.3; ev=[(burst+k*60/550,tick(2600,0.014,0.8),-0.5+k/20) for k in range(20)]
ev+=[(7.5,chime(990,0.8,0.5),0.3),(2.6,whoosh(0.7,0.25),0)]+[(8.5+0.4+j*0.42+0.4,tick(1500,0.02,0.6),-0.6+j*0.3) for j in range(5)]
build(16.1,ev,'G01_sfx')
# G02: Army BAR highlight, Marine regroup whoosh, link ticks, legend ticks
ev=[(2.6,chime(740,0.7,0.4),-0.5),(6.3,whoosh(1.4,0.45,250,1800),0.5)]+[(7.7+i*0.07,tick(2200,0.012,0.35),0.5) for i in range(9)]+[(t,tick(1600,0.02,0.5),0.4) for t in [8.4,9.6,10.8,12.0]]
build(19.7,ev,'G02_sfx')
# G03: columns rise (soft swell), magazines land (soft thuds), pocket outlines (ticks)
ev=[(2.0,swell(1.4,98,0.5),-0.4),(4.4,swell(1.1,130,0.35),-0.1),(6.1,thud(220,0.05,0.5),0.6),(9.8+0.75,thud(160,0.06,0.7),0.2)]+[(9.8+0.3+i*0.17,thud(150+i*4,0.05,0.6),0.2) for i in range(1,12)]+[(13.6+i*0.28+0.3,tick(1700,0.02,0.4),0.3) for i in range(4)]
build(16.7,ev,'G03_sfx')
# G04: typewriter keys for each typed line, pencil scratch for ridge, soft whoosh for the sketch shift
def typing(t0,n,dur): return [(t0+dur*k/n+rng.uniform(0,0.02),key(0.55),-0.5) for k in range(n)]
ev=typing(1.4,30,2.6)+typing(8.2,22,1.5)+typing(10.4,18,1.2)
ev+=[(6.6,whoosh(1.4,0.18,1500,6000),0.4),(13.6,whoosh(1.1,0.35),0.4),(14.6,tick(1200,0.03,0.5),0.4),(16.5,thud(200,0.05,0.4),0.5)]
build(21.5,ev,'G04_sfx')
# G05: each bar grows with a low swell and a tick when the count settles
ev=[]
for t0,f in [(3.4,100),(7.5,90),(14.0,115)]: ev+=[(t0,swell(1.7,f,0.45),0),(t0+1.6,tick(2000,0.02,0.6),0)]
build(19.4,ev,'G05_sfx')
# G06: 1957 node, rewind whoosh, node chimes, travel whooshes
ev=[(5.6,tick(1400,0.03,0.5),0.7),(9.9,chime(523,0.6,0.35),0.7),(15.4,whoosh(1.4,0.45,200,2200),-0.3),(16.8,chime(660,0.6,0.35),-0.7),
 (17.7,whoosh(1.5,0.25),-0.3),(19.2,chime(740,0.6,0.35),0),(20.4,whoosh(1.5,0.22),0.1),(22.0,chime(880,0.7,0.4),0.2),(23.4,whoosh(1.2,0.22),0.5),(24.6,thud(120,0.12,0.5),0.7)]
build(26.2,ev,'G06_sfx')
print('ok')
