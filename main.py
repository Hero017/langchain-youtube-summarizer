from summarizer.transcript import get_transcript
from summarizer.transcriber import transcribe_audio  # 👈 Add this
from summarizer.downloader import download_audio
from summarizer.summarizer import summarize_transcript
from summarizer.formatter import save_markdown, save_json, save_pdf, render_newsletter
from summarizer.utils import extract_quotes, extract_action_items
from summarizer.utils import detect_chapters
import os

def run_pipeline(video_url, category="misc", index=0):
    transcript = get_transcript(video_url)
    if not transcript:
        print("Transcript not found. Downloading audio...")
        audio_path = download_audio(video_url)
        transcript = transcribe_audio(audio_path)
        if not transcript:
            print("❌ Failed to get transcript")
            return

    print("Summarizing...")
    summary = summarize_transcript(transcript)

    from summarizer.utils import detect_chapters

    chapters = detect_chapters(transcript)
    chapter_text = "\n\n".join(
        f"## Chapter {i+1}\n\n{chunk}" for i, chunk in enumerate(chapters)
    )

    print("Extracting insights...")
    quotes = extract_quotes(summary)
    actions = extract_action_items(summary)

    full_summary = f"# Summary\n\n{summary}\n\n{chapter_text}\n\n## Quotes\n"
    full_summary += "\n".join(f'> "{q}"' for q in quotes)
    full_summary += "\n\n## Action Items\n" + "\n".join(f"- {a}" for a in actions)


    print("Saving outputs...")
    os.makedirs("samples", exist_ok=True)
    base_path = f"samples/{category}_{index}"

    save_markdown(full_summary, f"{base_path}.md")
    save_json(full_summary, f"{base_path}.json")
    save_pdf(full_summary, f"{base_path}.pdf")

    newsletter = render_newsletter(full_summary)
    with open(f"{base_path}_newsletter.html", "w", encoding="utf-8") as f:
        f.write(newsletter)

    print(f"✅ Done! Outputs saved as: {base_path}.*")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    if not url:
        print("❌ No URL provided. Exiting...")
        exit()
    run_pipeline(url)

