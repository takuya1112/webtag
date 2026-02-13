from core import (
    EmailPasswordWrongError,
    create_access_token,
)
from fastapi import APIRouter, HTTPException, status
from schemas.auth import LoginRequest, Token

from ..dependencies import UserServiceDep

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login", response_model=Token)
def login(
    service: UserServiceDep,
    data: LoginRequest,
):
    try:
        user = service.authenticate(data)
        access_token = create_access_token(user.public_id)
        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
    except EmailPasswordWrongError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password or Email is wrong.",
        )
