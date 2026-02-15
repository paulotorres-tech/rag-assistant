from fastapi import FastAPI

app = FastAPI(title="RAG Code Assistant", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
