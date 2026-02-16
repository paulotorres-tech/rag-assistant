from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from openai import OpenAI, OpenAIError
from app.models.schemas import (
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse,
    ChunckSource,
    EmbeddingRequest,
    EmbeddingResponse
)
from app.rag.llm_service import get_openai_client, chat, generate_embedding

app = FastAPI(title="RAG Code Assistant", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest):
    # Placeholder - we'll implement this later (Week 2)
    return IngestResponse(
        files_processed=0,
        chunks_created=0,
        message=f"Would ingest from {request.directory}"
    )

@app.post("/query", response_model=QueryResponse)
def query(
    request: QueryRequest,
    client: Annotated[OpenAI, Depends(get_openai_client)],
):
    result = chat(client, request.question)
    
    return QueryResponse(
        answer=result["answer"],
        sources=[],
        tokens_used=result["tokens_used"]
    )

@app.post("/embedding", response_model=EmbeddingResponse)
def embedding(
    request: EmbeddingRequest,
    client: Annotated[OpenAI, Depends(get_openai_client)],
):
    vector = generate_embedding(client, request.text)

    return EmbeddingResponse(
        embedding=vector,
        dimensions=len(vector),
        text_preview=request.text[:100],
    )