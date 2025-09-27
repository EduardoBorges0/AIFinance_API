from pydantic import BaseModel

class UpdateExpense(BaseModel):
    category: str
    value: float