from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import urlparse, parse_qs

from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    parsed_url = urlparse(url)

    # Case 1: Standard YouTube URL
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query)['v'][0]

    # Case 2: Short youtu.be URL
    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.strip("/")

    # Otherwise, return None or raise an error
    raise ValueError("Unsupported YouTube URL format")

def get_transcript(video_url):
    video_id = get_video_id(video_url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        return formatter.format_transcript(transcript)
    except:
        return None

