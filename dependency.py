from fastapi import APIRouter, Depends, Header, HTTPException


def authenticate_user(authorization: str = Header()):
    if authorization != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")