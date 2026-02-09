from fastapi import APIRouter, HTTPException, status
from ..dependencies import UserServiceDep
from schemas.auth import Token, LoginRequest
from core import (
    create_access_token,
    EmailPasswordWrongError,
) 


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/login", response_model=Token)
def login(
    service: UserServiceDep,
    form_data: LoginRequest, 
):  
    try:
        user = service.authenticate(form_data)
        access_token = create_access_token(str(user.public_id))
        return {
                "access_token": access_token,
                "token_type": "bearer",
        }
    except EmailPasswordWrongError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password or Email is wrong.",
        )
    