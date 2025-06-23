import yt_dlp
import imageio_ffmpeg
import os

def download_audio(video_url):
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

    output_path = 'downloads/audio.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Return the final path where audio is saved
    return os.path.join("downloads", "audio.mp3")
