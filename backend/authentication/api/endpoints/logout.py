from fastapi import APIRouter, status

from ..dependencies import LogoutDep
from ..schemas import LogoutRequest

router = APIRouter()


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    request: LogoutRequest,
    use_case: LogoutDep,
):
    use_case.execute(request.refresh_token)
