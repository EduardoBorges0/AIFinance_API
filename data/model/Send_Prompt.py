from dataclasses import dataclass
from pydantic import BaseModel

class SendPrompt(BaseModel):
    input: str
    user_id: int