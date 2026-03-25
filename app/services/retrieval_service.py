import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("data/vector_store/index.faiss")

chunks = json.load(open("data/processed/chunks.json"))


def retrieve(question, top_k=3):

    query_vector = model.encode([question])

    D, I = index.search(np.array(query_vector), top_k)

    results = []

    for idx in I[0]:
        results.append(chunks[idx])

    return results