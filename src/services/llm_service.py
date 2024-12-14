from openai import OpenAI
from typing import List
from src.config.settings import get_settings

settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.together.xyz",
            api_key=settings.TOGETHER_API_KEY,
        )
        
    async def get_response(self, question: str, context: List[str]) -> str:
        prompt = f"""Context: {' '.join(context)}
        
        Question: {question}
        
        Answer based on the context provided. If you cannot answer from the context, say so."""
        
        try:
            response = await self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful customer support AI."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=settings.MAX_TOKENS,
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM error: {str(e)}")
            raise