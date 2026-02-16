from fastapi import FastAPI
from app.models.schemas import (
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse
)

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
def query(request: QueryRequest):
    # Placeholder - we'll implement this later (Week 2)
    return QueryResponse(
        answer="Not implement yet",
        sources=[],
        tokens_used=0
    )