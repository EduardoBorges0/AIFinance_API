from fastapi import APIRouter
from service.AuthService import AuthService
from data.model.AuthModel import Token, UserRegister, UserLogin
from config.jwtconfig import hash_password

router = APIRouter()

@router.post("/login")
def login(userLogin: UserLogin):
    return AuthService.authenticate_user(userLogin.email, userLogin.password)

@router.post("/register")
def register(userRegister: UserRegister):
    hashpassword = hash_password(userRegister.password)
    return AuthService.register_user(userRegister.name, userRegister.email, hashpassword)

@router.get("/users/me")
def read_users_me():
    return AuthService.get_current_user()
