# 🎓 Campus Help Assistant — Mini RAG Chatbot

> A backend-only **Retrieval-Augmented Generation (RAG)** chatbot that answers student questions about campus policies using a handbook knowledge base.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| API Framework | FastAPI |
| Vector Database | FAISS |
| Embedding Model | Sentence Transformers |
| LLM Provider | Groq / OpenAI |
| Numerical Computing | NumPy |

---

## 🏗️ Project Architecture

The system follows a **RAG (Retrieval-Augmented Generation)** pipeline with two main phases:

---

### 📥 Phase 1 — Ingestion (Offline)

Prepares the knowledge base from the campus handbook.

```
read_handbook()
       ↓
chunk_text()
       ↓
save_chunks()
       ↓
generate_embeddings()
       ↓
create_vector_store()
```

Run ingestion with:

```bash
python -m scripts.ingest
```

**Output files created:**
- `data/processed/chunks.json`
- `data/vector_store/index.faiss`

---

### 🔍 Phase 2 — Query (Runtime)

When a user sends a question through the API:

```
User Question
       ↓
   retrieve()
       ↓
FAISS Vector Search
       ↓
Top Relevant Chunks
       ↓
  build_prompt()
       ↓
    ask_llm()
       ↓
LLM Generates Answer
       ↓
 API Returns Response
```

---

## 🌐 API Endpoint

### `POST /chat`

**Request:**
```json
{
  "question": "How many books can a student borrow?"
}
```

**Response:**
```json
{
  "answer": "Students can borrow up to 3 books at a time.",
  "sources": ["..."],
  "retrieved_chunks_count": 3
}
```

---

## 🧠 How Retrieval Works

1. Convert the user's question into a **vector embedding**
2. Search the **FAISS index** for the most similar vectors
3. Retrieve the **top matching chunks** from the handbook
4. Send the retrieved context + question to the **LLM**
5. Return the generated answer

> **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`

---

## 📁 Project Structure

```
mini-rag-backend/
│
├── app/
│   ├── api/
│   │   └── routes.py              # API route definitions
│   │
│   ├── core/
│   │   ├── config.py              # App configuration & env vars
│   │   └── models.py              # Pydantic request/response models
│   │
│   └── services/
│       ├── ingestion_service.py   # Chunking & embedding logic
│       ├── retrieval_service.py   # FAISS search logic
│       ├── prompt_service.py      # Prompt construction
│       └── llm_service.py         # LLM API calls
│
├── data/
│   ├── raw/
│   │   └── campus_handbook.txt    # Source knowledge base
│   ├── processed/
│   │   └── chunks.json            # Text chunks after splitting
│   └── vector_store/
│       └── index.faiss            # FAISS vector index
│
├── scripts/
│   └── ingest.py                  # Offline ingestion script
│
├── tests/
│   └── test_chat_api.py           # API tests
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Ingestion

```bash
python -m scripts.ingest
```

### 3. Start the FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

### 4. Open Interactive API Docs

```
http://127.0.0.1:8000/docs
```

---

## 💡 Key Concepts Used

- **Retrieval-Augmented Generation (RAG)** — Combining search + generation for grounded answers
- **Semantic Search** — Finding relevant text by meaning, not keywords
- **Vector Embeddings** — Representing text as numerical vectors
- **FAISS Vector Database** — Efficient similarity search at scale
- **Prompt Engineering** — Structuring context for better LLM responses
- **FastAPI Backend** — High-performance async Python API

---

## 🔮 Future Improvements

- [ ] Add a frontend UI
- [ ] Support multiple documents
- [ ] Add conversation history / memory
- [ ] Improve chunking strategy
- [ ] Add authentication & rate limiting

---

## 📄 License

This project is for educational purposes.
