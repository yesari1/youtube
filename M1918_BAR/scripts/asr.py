import json,glob,os
from faster_whisper import WhisperModel
m=WhisperModel('small.en',device='cpu',compute_type='int8')
out={}
for f in sorted(glob.glob('/tmp/claude-0/bar/voice/VO0*.mp3')):
    import subprocess,numpy as np
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    audio=np.frombuffer(raw,np.float32)
    segs,_=m.transcribe(audio,word_timestamps=True,language='en',beam_size=5)
    out[os.path.basename(f)[:4]]=[(w.word.strip(),round(w.start,2),round(w.end,2)) for s in segs for w in s.words]
    print(f,len(out[os.path.basename(f)[:4]]),flush=True)
json.dump(out,open('/tmp/claude-0/bar/voice/words.json','w'))
