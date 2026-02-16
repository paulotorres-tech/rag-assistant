from openai import OpenAI
from app.config import (
    AZURE_OPENAI_BASE_URL,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
)

def main():
    client = OpenAI(
        base_url=AZURE_OPENAI_BASE_URL,
        api_key=AZURE_OPENAI_API_KEY,
    )

    texts = [
        "How does authentication work in FastAPI?",
        "The login endpoint validates JWT tokens",
        "Making pasta with tomato sauce"
    ]

    response = client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=texts,
    )

    for i, item in enumerate(response.data):
        vector = item.embedding
        print(f"Text:   '{texts[i]}'")
        print(f"    Dimensions: {len(vector)}")
        print(f"    First 5 values: {vector[:5]}")
        print()

        # Simple similarity check
        # Texts 0 and 1 should be more similar then 0 and 2
        from math import sqrt

        def cosine_similarity(a: list[float], b: list[float]) -> float:
            dot = sum(x * y for x, y in zip(a, b))
            mag_a = sqrt(sum(x * x for x in a))
            mag_b = sqrt(sum(x * x for x in b))
            return dot / (mag_a * mag_b)
        
        v0 = response.data[0].embedding
        v1 = response.data[1].embedding
        v2 = response.data[2].embedding
        
        sim_auth = cosine_similarity(v0, v1)
        sim_pasta = cosine_similarity(v0, v2)

        print(f"Similarity (auth question <-> JWT answer): {sim_auth:.4f}")
        print(f"Similarity (auth question <-> pasta recipe): {sim_pasta:.4f}")
        print(f"\n{'Correct! ' if sim_auth > sim_pasta else 'Unexpected'} - related texts are more similar.")

if __name__ == "__main__":
    main()