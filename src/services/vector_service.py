import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict
from src.config.settings import get_settings
from src.utils.logger import logger

settings = get_settings()

class VectorService:
    def __init__(self):
        self.client = chromadb.Client(ChromaSettings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMA_PERSIST_DIR
        ))
        self.collection = self.client.get_or_create_collection("support_tickets")
    
    async def add_documents(self, texts: List[str], embeddings: List[List[float]], metadata: List[Dict]):
        """Add documents to vector store"""
        try:
            self.collection.add(
                embeddings=embeddings,
                documents=texts,
                metadatas=metadata,
                ids=[f"doc_{i}" for i in range(len(texts))]
            )
        except Exception as e:
            logger.error(f"Error adding documents to vector store: {str(e)}")
            raise
    
    async def search(self, query: str, query_embedding: List[float], n_results: int = 3):
        """Search for similar documents"""
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            return results
        except Exception as e:
            logger.error(f"Error searching vector store: {str(e)}")
            raise