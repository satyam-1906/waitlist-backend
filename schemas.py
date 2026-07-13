from pydantic import BaseModel

class WaitlistSchema(BaseModel):
    name: str
    email: str
    mobile_number: str
    location: str
    occupation: str