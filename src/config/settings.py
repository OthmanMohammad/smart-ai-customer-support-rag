from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    TOGETHER_API_KEY: str
    MODEL_NAME: str
    CHROMA_PERSIST_DIR: str
    MAX_TOKENS: int = 2000
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()