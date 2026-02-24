from fastapi import APIRouter

from ..dependencies import LoginDep
from ..schemas.validator import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(
    request: LoginRequest,
    use_case: LoginDep,
):
    access_token, refresh_token = use_case.execute(
        email=request.email,
        password=request.password,
    )
    return LoginResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )
