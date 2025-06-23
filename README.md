# LangChain YouTube Summarizer 🎥🧠

A Python-based summarizer that extracts transcripts, detects chapters, and generates structured summaries with insights from YouTube videos using LangChain, Whisper, and Hugging Face models.

## ✨ Features

- 🔗 YouTube URL input
- 📄 Transcript extraction (fallback to Whisper if needed)
- 🔊 Audio download & transcription
- 🧩 Chapter detection using sentence embeddings
- 💡 Key point & Action item extraction
- 🗣️ Quote highlighting
- 📤 Output formats:
  - Markdown (.md)
  - JSON (.json)
  - PDF (.pdf)
  - Newsletter HTML (.html)
- 🎬 Batch processing support

## 🛠️ Tech Stack

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- OpenAI Whisper (fallback transcription)
- Hugging Face Transformers (Summarization)
- Sentence Transformers (Chapter detection)
- yt-dlp + ffmpeg
- Jinja2 for newsletter
- FPDF for PDFs

## 📁 Project Structure

YT_summarizer_project/
│
├── summarizer/ # Core modules (downloader, transcriber, summarizer)
├── templates/ # Jinja2 newsletter template
├── outputs/ # Output files (.md, .json, .pdf, .html)
├── main.py # Entry point
├── batch_runner.py # Batch video runner
├── requirements.txt
└── README.md


#### ✅ How to Run
```markdown
## 🚀 Run the Project

1. Clone this repo
2. Set up virtual env:
   ```bash
   python -m venv yt_env
   yt_env\Scripts\activate
   pip install -r requirements.txt

Run:  python main.py(for single video)
      python batch_runner.py(for multiple videos)

## 🧾 Notes

- This tool uses Whisper when YouTube captions are unavailable.
- Long videos are chunked for accurate summarization.
- Chapter detection is based on cosine similarity between sentence embeddings.
