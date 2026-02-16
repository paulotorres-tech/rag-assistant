from pydantic import BaseModel, Field

class IngestRequest(BaseModel):
    """Request to ingest documents from a directory."""
    directory: str = Field(..., description="Path to the directory to ingest")
    fi_extensions: list[str] = Field(
        defautl=[".py", ".md", ".cs", ".json"],
        description="File extensions to include"
    )

class IngestResponse(BaseModel):
    """Response after ingesting documents."""
    files_processed: int
    chunks_created: int
    message: str

class QueryRequest(BaseModel):
    """Resquest to query the RAG system."""
    question: str = Field(..., min_length=1, max_length=1000)
    max_results: int = Field(default=5, ge=1, le=20)

class ChunckSource(BaseModel):
    """A source chunch that was retrieved."""
    file_path: str
    chunk_index: int
    content_preview: str = Field(..., max_length=200)
    relevance_score: float

class QueryResponse(BaseModel):
    """Response from the RAG query."""
    answer: str
    sources: list[ChunckSource]
    tokens_used: int