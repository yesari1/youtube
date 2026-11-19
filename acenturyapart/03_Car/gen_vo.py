# Run on Yunus's PC (ELEVENLABS_API_KEY in user env). Writes vo/<chunk>.mp3 next to this file.
import os, sys, json, urllib.request, time
P = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, P)
from script import CHUNKS
KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE = "ppLqTilh7rH7fbUVlXsf"  # David - Documentary
TAG = {"hook": "intrigued", "price": "matter-of-fact", "credit": "thoughtful", "factory": "curious", "car": "warm", "starter": "thoughtful",
       "today": "calm", "license": "measured", "roads": "serious", "numbers": "reflective", "verdict": "warm"}
os.makedirs(f"{P}/vo", exist_ok=True)
only = sys.argv[1:]
for cid, gap, ss in CHUNKS:
    if only and cid not in only: continue
    out = f"{P}/vo/{cid}.mp3"
    if os.path.exists(out) and not only: continue
    text = f"[{TAG[cid]}] " + " [short pause] ".join(t for _, t in ss)
    body = {"text": text, "model_id": "eleven_v4",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "speed": 1.0}}
    for attempt in range(3):
        try:
            req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_192",
                data=json.dumps(body).encode(), headers={"xi-api-key": KEY, "Content-Type": "application/json"})
            data = urllib.request.urlopen(req, timeout=300).read(); open(out, "wb").write(data)
            print("OK", cid, len(data)); break
        except Exception as e:
            msg = getattr(e, "read", lambda: b"")().decode(errors="ignore")[:300]
            print("ERR", cid, e, msg); time.sleep(5)
