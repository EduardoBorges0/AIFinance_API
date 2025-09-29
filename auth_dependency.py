# auth_dependency.py
from fastapi import Header, HTTPException, Depends
from config.jwtconfig import verify_token

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = authorization.replace("Bearer ", "")
    auth = verify_token(token)

    if auth is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return auth  # Pode ser o user_id ou payload do token
