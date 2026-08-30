# POST /login

from fastapi import Depends
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import BaseToken
from dependency import get_current_user
# defin router
router = APIRouter()

@router.post("/login", response_model=BaseToken)

async def login(formdata:OAuth2PasswordRequestForm = Depends()):
    if formdata.username == "admin" and formdata.password == "admin":
        return {
            "access_token": "valid_token",
            "token_type": "bearer"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
