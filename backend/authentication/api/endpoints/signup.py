from fastapi import APIRouter

from ..dependencies import SignupDep
from ..schemas import SignupRequest, SignupResponse

router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
def signup(
    request: SignupRequest,
    use_case: SignupDep,
):
    access_token, refresh_token = use_case.execute(
        name=request.name,
        email=request.email,
        password=request.password,
    )
    return SignupResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )
