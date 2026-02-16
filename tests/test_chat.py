from openai import OpenAI
from app.config import (
    AZURE_OPENAI_BASE_URL,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_CHAT_DEPLOYMENT,
)

def main():
    client = OpenAI(
        base_url=AZURE_OPENAI_BASE_URL,
        api_key=AZURE_OPENAI_API_KEY,
    )

    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": "Explain what RAG means in 2 sentences."},
        ],
        max_tokens=200,
        temperature=0.7,
    )

    print("Response:")
    print(response.choices[0].message.content)
    print(f"\nTokens used: {response.usage.total_tokens}")

if __name__ == "__main__":
    main()