import numpy as np
from app.services.ingestion_service import (
    read_handbook,
    chunk_text,
    save_chunks,
    generate_embeddings,
    create_vector_store
)

print("Reading handbook...")

text = read_handbook()

print("Chunking text...")

chunks = chunk_text(text)

save_chunks(chunks)

print("Generating embeddings...")

embeddings = generate_embeddings(chunks)

print("Creating vector store...")

create_vector_store(np.array(embeddings))

print("Ingestion complete")