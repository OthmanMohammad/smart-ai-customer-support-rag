from pydantic import BaseModel
from typing import Optional, List

class SupportTicket(BaseModel):
    ticket_id: str
    customer_name: str
    product_purchased: str
    ticket_type: str
    ticket_subject: str
    ticket_description: str
    ticket_status: str
    ticket_priority: str

class ChatMessage(BaseModel):
    question: str
    context: Optional[List[str]] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[dict]
    confidence: float