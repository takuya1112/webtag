from fastapi import APIRouter, HTTPException, status
from ..dependencies import UserServiceDep
from schemas.user import UserCreate, UserResponse
from core.exceptions import EmailAlreadyExistsError

router = APIRouter(
    prefix="/users",
    tags=["User"],
)

@router.post("/", response_model=UserResponse, status_code=201)
def post(
    service: UserServiceDep,
    create_data: UserCreate,
):
    try:
        return service.create(create_data)
    except EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
