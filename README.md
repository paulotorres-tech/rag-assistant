# RAG Code Assistant

An AI-powered code documentation assistant that answers questions about codebases using Retrieval-Augmented Generation (RAG).

## What It Does

- Ingests code files and documentation
- Generates embeddings for semantic search
- Answers questions grounded in your actual code

## Tech Stack

- **Python** — FastAPI for the API layer
- **Azure OpenAI** — GPT-4o for chat, text-embedding-3-small for embeddings
- **ChromaDB** — Vector database for semantic search (coming Week 2)

## Current Status

**Week 1 Complete:**
- FastAPI API with 4 endpoints
- Azure OpenAI integration (chat + embeddings)
- Pydantic models for request/response validation
- Error handling for upstream service failures

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /query | Ask a question, get an LLM-powered answer |
| POST | /embedding | Generate an embedding vector for text |
| POST | /ingest | Ingest documents (placeholder) |

## Setup

1. Clone the repo
2. Create virtual environment: `python -m venv .venv`
3. Activate: `.\.venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your Azure OpenAI credentials
6. Run: `python -m uvicorn app.main:app --reload`
7. Open: http://localhost:8000/docs

## Next Steps (Week 2)

- Document loading (Python, Markdown, C# files)
- Text chunking with configurable size and overlap
- ChromaDB vector storage
- Semantic search retrieval
- Full RAG pipeline: ingest → embed → store → retrieve → answer
