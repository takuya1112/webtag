from fastapi import APIRouter, HTTPException, status

from ...exceptions import ExpiredTokenError, InvalidTokenError, TokenStolenError
from ..dependencies import RefreshAccessTokenDep
from ..schemas import RefreshTokenRequest, RefreshTokenResponse

router = APIRouter()


@router.post("/refresh", response_model=RefreshTokenResponse)
def refresh_access_token(
    request: RefreshTokenRequest,
    use_case: RefreshAccessTokenDep,
):
    try:
        new_refresh_token = use_case.execute(request.refresh_token)
        new_access_token = "abcdefg"

        return RefreshTokenResponse(
            refresh_token=new_refresh_token,
            access_token=new_access_token,
        )
    except ExpiredTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="hehehe",
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="hehehe",
        )
    except TokenStolenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="hehehe",
        )
