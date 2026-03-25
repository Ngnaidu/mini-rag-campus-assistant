# Campus Help Assistant (Mini RAG Chatbot)

A backend-only Retrieval-Augmented Generation (RAG) chatbot that answers questions about campus policies using a handbook knowledge base.

## Tech Stack

- Python
- FastAPI
- FAISS (Vector Database)
- Sentence Transformers
- LLM API (Groq / OpenAI)
- NumPy

---

# Project Architecture

The system follows a **RAG (Retrieval-Augmented Generation)** architecture.

Two main phases:

1. Ingestion Phase (Offline)
2. Query Phase (Runtime)

---

# Ingestion Phase (Offline)

This phase prepares the knowledge base.

Steps:

1. Read the handbook
2. Split it into chunks
3. Generate embeddings
4. Store vectors in FAISS database

Flow:


read_handbook()
↓
chunk_text()
↓
save_chunks()
↓
generate_embeddings()
↓
create_vector_store()


Run ingestion with:


python -m scripts.ingest


This creates:


data/processed/chunks.json
data/vector_store/index.faiss


---

# Query Phase (Runtime)

When a user asks a question through the API:

Flow:


User Question
↓
retrieve()
↓
FAISS vector search
↓
top relevant chunks
↓
build_prompt()
↓
ask_llm()
↓
LLM generates answer
↓
API returns response


---

# API Endpoint

POST `/chat`

Example request:

```json
{
 "question": "How many books can a student borrow?"
}

Example response:

{
 "answer": "Students can borrow up to 3 books at a time.",
 "sources": [...],
 "retrieved_chunks_count": 3
}
How Retrieval Works
Convert user question into an embedding.
Search FAISS index for similar vectors.
Retrieve top matching chunks.
Send context + question to LLM.

Embedding model used:

sentence-transformers/all-MiniLM-L6-v2
Project Structure
mini-rag-backend
│
├── app
│   ├── api
│   │   └── routes.py
│   │
│   ├── core
│   │   ├── config.py
│   │   └── models.py
│   │
│   └── services
│       ├── ingestion_service.py
│       ├── retrieval_service.py
│       ├── prompt_service.py
│       └── llm_service.py
│
├── data
│   ├── raw
│   │   └── campus_handbook.txt
│   ├── processed
│   │   └── chunks.json
│   └── vector_store
│       └── index.faiss
│
├── scripts
│   └── ingest.py
│
├── tests
│   └── test_chat_api.py
│
├── requirements.txt
└── README.md
How to Run the Project
1 Install dependencies
pip install -r requirements.txt
2 Run ingestion
python -m scripts.ingest
3 Start FastAPI server
python -m uvicorn app.main:app --reload
4 Open API docs
http://127.0.0.1:8000/docs
Key Concepts Used
Retrieval-Augmented Generation (RAG)
Semantic Search
Vector Embeddings
FAISS Vector Database
Prompt Engineering
FastAPI Backend
Future Improvements
Add frontend UI
Support multiple documents
Add conversation history
Improve chunking strategy

---

# 3️⃣ Push README to GitHub

Run:

```bash
git add README.md
git commit -m "Add project README"
git push
Result

Your GitHub repo will now look professional and contain:

README.md
app/
scripts/
data/
requirements.txt