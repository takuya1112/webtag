from fastapi import APIRouter, HTTPException, status
from ...schemas import EmailAlreadyExistsError, UserCreate, UserResponse
from ..dependencies import UserServiceDep

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.post("/", response_model=UserResponse, status_code=201)
def post(
    create_data: UserCreate,
    service: UserServiceDep
):
    try:
        return service.create(create_data)
    except EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
