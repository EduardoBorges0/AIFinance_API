from dataclasses import dataclass

@dataclass
class ExpenseData:
    categoria: str
    valor: float
    user_id: int
    id: int = 0
