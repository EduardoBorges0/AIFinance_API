from fastapi import APIRouter, Depends, HTTPException
from dataclasses import asdict
from fastapi.encoders import jsonable_encoder
from service.OpenAIService import OpenAIService
from data.model.Send_Prompt import SendPrompt
from data.model.UpdateExpenseModel import UpdateExpense
from data.model.ExpenseData import ExpenseData
from auth_dependency import get_current_user

router = APIRouter()
service = OpenAIService()


@router.post("/create_expense")
def create_expense(text: SendPrompt, user=Depends(get_current_user)):
    try:
        service.insert_expense_db(text.input, user)
        return {"message": "Expense created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_expense/{id}")
def delete_expense(id: int, user=Depends(get_current_user)):
    try:
        service.remove_expense_db(id)
        return {"message": f"Expense {id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_expense/{id}")
def update_expense(id: int, expense: UpdateExpense, user=Depends(get_current_user)):
    try:
        service.update_expense_db(id, expense.category, expense.value)
        return {"message": f"Expense {id} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_expenses")
def get_expenses(user=Depends(get_current_user)):
    expenses = service.get_expenses_db()
    expenses_objects = [
        ExpenseData(id=e[0], categoria=e[1], valor=float(e[2]), user_id=e[3])
        for e in expenses
    ]
    return jsonable_encoder({"expenses": [asdict(exp) for exp in expenses_objects]})
