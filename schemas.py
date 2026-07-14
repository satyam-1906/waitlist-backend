from pydantic import BaseModel
from typing import Dict, Any

class WaitlistSchema(BaseModel):
    name: str
    email: str
    mobile_number: str
    location: str
    occupation: str
    details: Dict[str, Any]