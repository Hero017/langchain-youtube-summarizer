# summarizer/utils.py
import re

def extract_quotes(text):
    return re.findall(r'"(.*?)"', text)

def extract_action_items(text):
    return [line for line in text.split('\n') if line.strip().startswith("•") or "should" in line or "must" in line]

from sentence_transformers import SentenceTransformer, util

# Load the model only once (outside the function for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')

def detect_chapters(transcript: str, chunk_size: int = 5):
    sentences = transcript.split(". ")
    chapters = []
    current_chunk = []
    previous_embedding = None

    for sentence in sentences:
        current_chunk.append(sentence.strip())
        if len(current_chunk) >= chunk_size:
            chunk_text = ". ".join(current_chunk)
            embedding = model.encode(chunk_text, convert_to_tensor=True)

            if previous_embedding is not None:
                similarity = util.pytorch_cos_sim(embedding, previous_embedding).item()
                if similarity < 0.8:
                    chapters.append(". ".join(current_chunk))
                    current_chunk = []
            previous_embedding = embedding

    if current_chunk:
        chapters.append(". ".join(current_chunk))

    return chapters
