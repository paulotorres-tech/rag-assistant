from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_openai_base_url: str
    azure_openai_api_key: str
    azure_openai_chat_deployment: str = "gpt-4o"
    azure_openai_embedding_deployment: str = "text-embedding-3-small"

    class Config:
        env_file = ".env"

settings = Settings()