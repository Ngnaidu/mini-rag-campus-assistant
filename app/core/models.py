from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    question: str

class Source(BaseModel):
    chunk_id: str
    section_title: str
    source_file: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    retrieved_chunks_count: int

class Chunk(BaseModel):
    chunk_id: str
    section_title: str
    text: str
    source_file: str