from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()


def authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != "secret123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication"
        )