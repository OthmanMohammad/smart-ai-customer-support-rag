from openai import OpenAI
from typing import List
import numpy as np
from src.config.settings import get_settings
from src.utils.logger import logger

settings = get_settings()

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.together.xyz",
            api_key=settings.TOGETHER_API_KEY
        )
    
    async def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts"""
        try:
            embeddings = []
            for text in texts:
                response = await self.client.embeddings.create(
                    model="togethercomputer/m2-bert-80M-8k-retrieval",
                    input=text
                )
                embeddings.append(response.data[0].embedding)
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise EmbeddingError(f"Failed to generate embeddings: {str(e)}")