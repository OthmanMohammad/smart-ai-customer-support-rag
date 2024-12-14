import asyncio
from src.services.data_service import DataService
from src.services.embedding_service import EmbeddingService
from src.services.vector_service import VectorService
from src.utils.logger import logger

async def main():
    try:
        # Load and process data
        data_service = DataService()
        processed_docs = data_service.load_and_process_data()
        
        # Generate embeddings
        embedding_service = EmbeddingService()
        texts = [doc['text'] for doc in processed_docs]
        embeddings = await embedding_service.get_embeddings(texts)
        
        # Store in vector database
        vector_service = VectorService()
        metadata = [doc['metadata'] for doc in processed_docs]
        await vector_service.add_documents(texts, embeddings, metadata)
        
        logger.info("Data processing complete!")
    except Exception as e:
        logger.error(f"Error in data processing: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())