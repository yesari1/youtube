"""post.py <dir> <name> <dur> : average subframes, Lanczos downscale, grain+flicker, encode H.264 CRF 10 60fps + preview + contact sheet."""
import os,sys,glob,subprocess,numpy as np
from PIL import Image
D,name,dur=sys.argv[1],sys.argv[2],float(sys.argv[3]); FPS=60; N=round(dur*FPS)
os.makedirs(f'{D}/out',exist_ok=True)
def one(i):
    rng=np.random.default_rng(1918+i)
    fs=sorted(glob.glob(f'{D}/sub/s_{i:05d}_*.*'))
    acc=sum(np.asarray(Image.open(f).convert('RGB'),np.float32) for f in fs)/len(fs)
    img=Image.fromarray(acc.clip(0,255).astype(np.uint8))
    if img.size!=(1920,1080): img=img.resize((1920,1080),Image.LANCZOS)
    a=np.asarray(img,np.float32)
    g=rng.normal(0,1,(540,960)).astype(np.float32)
    g=np.asarray(Image.fromarray(((g*40)+128).clip(0,255).astype(np.uint8)).resize((1920,1080),Image.BICUBIC),np.float32)-128
    lum=a.mean(2,keepdims=True)/255
    a=a+g[...,None]*(0.05+0.06*(1-lum))
    a*=1+0.006*np.sin(i*0.9)+0.004*rng.standard_normal()
    Image.fromarray(a.clip(0,255).astype(np.uint8)).save(f'{D}/out/f_{i:05d}.png',compress_level=1)
if __name__=='__main__':
    from multiprocessing import Pool
    with Pool(4) as p: p.map(one,range(N),chunksize=8)
    enc=['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{D}/out/f_%05d.png']
    subprocess.run(enc+['-c:v','libx264','-pix_fmt','yuv420p','-crf','10','-preset','slow','-tune','film','-movflags','+faststart',f'{D}/{name}.mp4'],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{D}/{name}.mp4','-vf','scale=960:-2','-r','30','-c:v','libx264','-crf','28','-preset','fast',f'{D}/{name}_preview.mp4'],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{D}/{name}.mp4','-vf',f'fps=16/{dur},scale=480:-1,tile=4x4','-frames:v','1',f'{D}/{name}_contact.jpg'],check=True)
    print('done',name)
