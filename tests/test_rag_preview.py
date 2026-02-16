from app.rag.llm_service import get_openai_client, chat

def main():
    client = get_openai_client()

    #Simulate retrieved code chunks
    context = """
# File: app/main.py
from fastapi import FastAPI, Depends
from openai import OpenAI
from app.rag.llm_service import get_openai_client, chat

app = FastAPI(title="RAG Code Assistant", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(request: QueryRequest, client: AzureOpenAI = Depends(get_openai_client)):
    result = chat(client, request.question)
    return QueryResponse(answer=result["answer"], sources=[], tokens_used=result["tokens_used"])

# File: app/rag/llm_service.py
def get_openai_client() -> AzureOpenAI:
    return OpenAI(
        base_url=settings.azure_openai_base_url,
        api_key=settings.azure_openai_api_key,
    )

def chat(client: AzureOpenAI, question: str, context: str = "") -> dict:
    messages = [{"role": "system", "content": system_prompt}]
    if context:
        messages.append({"role": "user", "content": f"Context:\\n{context}\\n\\nQuestion: {question}"})
    response = client.chat.completions.create(model=settings.azure_openai_chat_deployment, messages=messages)
    return {"answer": response.choices[0].message.content, "tokens_used": response.usage.total_tokens}"""

    questions = [
        "How does dependency injection work in this project?",
        "What happens when someone calls the /query endpoint?",
        "Where are the Azure OpenAI credentials configured?",
    ]

    for question in questions:
        print(f"\n{'='*60}")
        print(f"Q: {question}")
        print(f"{'='*60}")
        result = chat(client, question, context=context)
        print(f"A: {result['answer']}")
        print(f"Tokens: {result['tokens_used']}")

if __name__ == "__main__":
    main();