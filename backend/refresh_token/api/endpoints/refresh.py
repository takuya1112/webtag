from fastapi import APIRouter

from ..dependencies import RefreshAccessTokenDep
from ..schemas import RefreshTokenRequest, RefreshTokenResponse

router = APIRouter()


@router.post("/refresh", response_model=RefreshTokenResponse)
def refresh_access_token(
    request: RefreshTokenRequest,
    use_case: RefreshAccessTokenDep,
):
    new_refresh_token = use_case.execute(request.refresh_token)
    new_access_token = "abcdefg"

    return RefreshTokenResponse(
        refresh_token=new_refresh_token,
        access_token=new_access_token,
    )
