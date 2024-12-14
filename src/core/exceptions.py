class DataProcessingError(Exception):
    """Raised when there's an error processing the data"""
    pass

class EmbeddingError(Exception):
    """Raised when there's an error generating embeddings"""
    pass

class LLMError(Exception):
    """Raised when there's an error with the LLM service"""
    pass