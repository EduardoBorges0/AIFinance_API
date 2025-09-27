# controller/expense_controller.py
from fastapi import APIRouter, HTTPException
from dataclasses import asdict
from fastapi.encoders import jsonable_encoder
from service.OpenAIService import OpenAIService
from data.model.Send_Prompt import SendPrompt
from data.model.UpdateExpenseModel import UpdateExpense
from data.model.ExpenseData import ExpenseData

router = APIRouter()
service = OpenAIService()

@router.post("/create_expense")
def create_expense(text: SendPrompt):
    try:
        service.insert_expense_db(text.input, text.user_id)
        return {"message": "Expense created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_expense/{id}")
def delete_expense(id: int):
    try:
        service.remove_expense_db(id)
        return {"message": f"Expense {id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_expense/{id}")
def update_expense(id: int, expense: UpdateExpense):
    try:
        service.update_expense_db(id, expense.category, expense.value)
        return {"message": f"Expense {id} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_expenses")
def get_expenses():
    try:
        expenses = service.get_expenses_db()
        expenses_objects = [ExpenseData(id=e[0], categoria=e[1], valor=float(e[2])) for e in expenses]
        return jsonable_encoder({"expenses": [asdict(exp) for exp in expenses_objects]})
    except Exception as e:
        return {"error": str(e)}
