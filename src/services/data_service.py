import pandas as pd
from typing import List
import logging

logger = logging.getLogger(__name__)

class DataService:
    def __init__(self):
        self.raw_data_path = "data/raw/support_tickets.csv"
        
    def load_and_process_data(self) -> List[dict]:
        df = pd.read_csv(self.raw_data_path)
        
        processed_docs = []
        for _, row in df.iterrows():
            doc = {
                'text': f"""
                Question: {row['Ticket Subject']}
                Description: {row['Ticket Description']}
                Product: {row['Product Purchased']}
                """,
                'metadata': {
                    'ticket_id': row['Ticket ID'],
                    'product': row['Product Purchased'],
                    'type': row['Ticket Type'],
                    'priority': row['Ticket Priority']
                }
            }
            processed_docs.append(doc)
            
        return processed_docs