from fastapi import APIRouter

from ..dependencies import LogoutDep

router = APIRouter()


@router.post("/logout")
def logout(
    request,
    use_case: LogoutDep,
):
    use_case.execute()
