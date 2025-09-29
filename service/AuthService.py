from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.jwtconfig import hash_password, verify_password, create_access_token, verify_token
from data.repository.AuthRepository import AuthRepository
from data.model.AuthModel import UserLogin
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    @staticmethod
    def register_user(name: str, email: str, password: str):
        AuthRepository.register_user(name, email, password)

    @staticmethod
    def get_user_by_email(email: str):
        return AuthRepository.get_user_by_email(email)

    @staticmethod
    def authenticate_user(email: str, password: str):
        user = AuthService.get_user_by_email(email)
        if not user:
            return False
        if not verify_password(password, user["password"]):
            return False

        return user

    @staticmethod
    def login(userLogin: UserLogin):
        user = AuthService.authenticate_user(userLogin.email, userLogin.password)
        if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

        access_token = create_access_token(data={"sub": str(user["id"])})
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)):
        user_id = verify_token(token)
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return user_id

    @staticmethod
    def read_users_me(current_user: int = Depends(get_current_user)):
        return {"user_id": current_user}

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)):
        user_id = verify_token(token)  # pega o "sub" do JWT
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        user = AuthRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        return user
