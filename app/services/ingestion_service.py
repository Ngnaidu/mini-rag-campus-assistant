import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def read_handbook(path="data/raw/campus_handbook.txt"):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text:
        raise ValueError("Knowledge base is empty")

    return text


def chunk_text(text):

    sections = text.split("Section")[1:]

    chunks = []

    for i, section in enumerate(sections):

        title = section.split("\n")[0].strip()

        content = "Section " + section

        chunk = {
            "chunk_id": f"chunk_{i+1}",
            "section_title": title,
            "text": content,
            "source_file": "campus_handbook.txt"
        }

        chunks.append(chunk)

    return chunks


def save_chunks(chunks):

    with open("data/processed/chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)


def generate_embeddings(chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    return embeddings


def create_vector_store(embeddings):

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings))

    faiss.write_index(index, "data/vector_store/index.faiss")