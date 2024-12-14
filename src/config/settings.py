from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    TOGETHER_API_KEY: Optional[str] = None
    MODEL_NAME: str
    CHROMA_PERSIST_DIR: str
    MAX_TOKENS: int = 2000
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"

@lru_cache()
def get_settings():
    return Settings()