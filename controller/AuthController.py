from fastapi import APIRouter, Depends
from service.AuthService import AuthService
from data.model.AuthModel import Token, UserRegister, UserLogin
from config.jwtconfig import hash_password
from auth_dependency import get_current_user

router = APIRouter()

@router.post("/login")
def login(userLogin: UserLogin):
    return AuthService.login(userLogin)


@router.get("/me")
def read_users_me(current_user: dict = Depends(AuthService.get_current_user), user=Depends(get_current_user)):
    return {"id": current_user["id"], "name": current_user["name"], "email": current_user["email"]}


@router.post("/register")
def register(userRegister: UserRegister):
    hashpassword = hash_password(userRegister.password)
    return AuthService.register_user(userRegister.name, userRegister.email, hashpassword)
