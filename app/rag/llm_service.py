from openai import OpenAI
from app.config import settings

def get_openai_client() -> OpenAI:
    return OpenAI(
        base_url=settings.azure_openai_base_url,
        api_key=settings.azure_openai_api_key,
    )

def chat(client: OpenAI, question: str, context: str = "") -> dict:
    """Send a question to Azure OpenAI, optionally with context."""

    system_prompt = """You are a helpful code documentation assistant.
    Answer questions about code clearly and concisely.
    If context is provided, base your answer on that context.
    If you don't know the answer, say so - don't make things up."""

    messages = [{
        "role": "system", 
        "content": system_prompt}]

    if context:
        messages.append({
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        })
    else:
        messages.append({
            "role": "user",
            "content": question
        })

    response = client.chat.completions.create(
        model=settings.azure_openai_chat_deployment,
        messages=messages,
        max_tokens=500,
        temperature=0.3,
    )

    return {
        "answer": response.choices[0].message.content,
        "tokens_used": response.usage.total_tokens,
    }

def generate_embedding(client: OpenAI, text: str) -> list[float]:
    """Generate an embedding vector for a text."""
    response = client.embeddings.create(
        model=settings.azure_openai_embedding_deployment,
        input=[text],
    )
    return response.data[0].embedding