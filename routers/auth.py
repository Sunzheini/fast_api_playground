from datetime import timedelta, datetime, timezone
from typing import Dict, Any, Optional
import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError

from models.temp_db import DataBaseManager

router = APIRouter()

# ✅ Get secret key from environment variables (secure)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-for-development-only")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/login")
async def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and return JWT token

    Uses standard OAuth2 form format:
    - username: the user identifier
    - password: the user password (if applicable)
    """
    db = DataBaseManager()

    user = db.get_user_by_username(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # In a real app, verify password here
    # if not verify_password(form_data.password, user.hashed_password):
    #     raise HTTPException(...)

    access_token = create_access_token(
        username=user.name,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def create_access_token(username: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token

    Args:
        username: The subject of the token
        expires_delta: Optional timedelta for token expiration

    Returns:
        Encoded JWT token
    """
    to_encode: Dict[str, Any] = {"sub": username}

    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expires})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.get("/verify-token")
async def verify_token(token: str):
    """
    Verify if a JWT token is valid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        return {"username": username, "valid": True}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
