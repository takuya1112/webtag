from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import TagService

router = APIRouter(
    prefix="/tags",
    tags=["Tag"]
)

def get_tag_service(
        session: Session = Depends(get_session)
        ) -> TagService:
    return TagService(session)

class TagCreate(BaseModel):
    name: str

class TagUpdate(BaseModel):
    name: str

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class DeleteAllResponse(BaseModel):
    deleted_count: int

@router.post("/", response_model=TagResponse)
def create(
    tag: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    return service.create(name=tag.name)

@router.delete("/{tag_id}", response_model=TagResponse)
def hard_delete(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    return service.hard_delete(tag_id)

@router.delete("/", response_model=DeleteAllResponse)
def hard_delete_all(
    service: TagService = Depends(get_tag_service)
):
    deleted_count = service.hard_delete_all()
    return {"deleted_count": deleted_count}

@router.get("/{tag_id}", response_model=TagResponse)
def read(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    return service.read(tag_id)

@router.get("/", response_model=list[TagResponse])
def read_all(
    service: TagService = Depends(get_tag_service)
):
    return service.read_all()

@router.put("/{tag_id}", response_model=TagResponse)
def update(
    tag_id: int,
    tag: TagUpdate,
    service: TagService = Depends(get_tag_service)
):
    return service.update(tag_id=tag_id, new_name=tag.name)