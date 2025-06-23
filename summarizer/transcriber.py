# summarizer/transcriber.py

import whisper
import os
from imageio_ffmpeg import get_ffmpeg_exe

# Step 1: Ensure ffmpeg path is set properly (LOCAL fix)
ffmpeg_path = get_ffmpeg_exe()
os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ.get("PATH", "")

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # You can change to "small" or "medium"
    result = model.transcribe(audio_path)
    return result["text"]


