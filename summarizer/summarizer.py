# summarizer/summarizer.py
from transformers import pipeline
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def split_text(text, max_tokens=512, overlap=50):
    tokens = tokenizer.encode(text, add_special_tokens=False)
    chunks = []
    start = 0
    end = max_tokens

    while start < len(tokens):
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)
        start = end - overlap
        end = start + max_tokens

    return chunks

def summarize_transcript(transcript):
    chunks = split_text(transcript)  # ✅ Use safe tokenizer-based split function
    summaries = []

    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summaries.append(result[0]["summary_text"])

    return "\n\n".join(summaries)

