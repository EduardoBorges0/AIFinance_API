# main.py
from fastapi import FastAPI
from controller.AuthController import router as auth_router
from controller.OpenAIController import router as expense_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(expense_router, prefix="/api")
