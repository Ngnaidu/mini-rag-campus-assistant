# from fastapi import APIRouter
# from app.core.models import ChatRequest
# from app.services.retrieval_service import retrieve

# router = APIRouter()

# @router.post("/chat")
# def chat(req: ChatRequest):

#     question = req.question.lower()

#     retrieved_chunks = retrieve(question)


#     if "revaluation" in question:
#         answer = "The revaluation fee is 500 rupees per subject."

#     elif "attendance" in question:
#         answer = "Students must maintain at least 75 percent attendance."

#     elif "book" in question or "borrow" in question:
#         answer = "Students can borrow up to 3 books at a time from the library."

#     elif "hostel" in question:
#         answer = "A grace period of 7 days is allowed after the hostel fee due date."

#     elif "id card" in question:
#         answer = "The duplicate ID card fee is 300 rupees."

#     else:
#         answer = "I do not have enough information in the provided knowledge base to answer that."

#     return {
#         "answer": answer,
#         "sources": retrieved_chunks,
#         "retrieved_chunks_count": len(retrieved_chunks)
#     }


from fastapi import APIRouter
from app.core.models import ChatRequest
from app.services.retrieval_service import retrieve
from app.services.prompt_service import build_prompt
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):

    # Step 1: Read user question
    question = req.question.strip()

    if not question:
        return {"error": "Question cannot be empty"}

    # Step 2: Retrieve relevant chunks from FAISS vector store
    retrieved_chunks = retrieve(question)

    # Step 3: Build prompt using retrieved context
    prompt = build_prompt(question, retrieved_chunks)

    # Step 4: Send prompt to LLM
    answer = ask_llm(prompt)

    # Step 5: Return answer + sources
    return {
        "answer": answer,
        "sources": retrieved_chunks,
        "retrieved_chunks_count": len(retrieved_chunks)
    }






