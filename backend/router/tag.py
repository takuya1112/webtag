from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import TagService

tag_router = APIRouter(
    prefix="/tag",
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

@tag_router.post("/", response_model=TagResponse)
def create(
    tag: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    return service.create(name=tag.name)

@tag_router.delete("/{tag_id}", response_model=TagResponse)
def delete(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    return service.delete(tag_id)

@tag_router.delete("/", response_model=DeleteAllResponse)
def delete_all(
    service: TagService = Depends(get_tag_service)
):
    deleted_count = service.delete_all()
    return {"deleted_count": deleted_count}

@tag_router.get("/{tag_id}", response_model=TagResponse)
def read(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    return service.read(tag_id)

@tag_router.get("/", response_model=list[TagResponse])
def read_all(
    service: TagService = Depends(get_tag_service)
):
    return service.read_all()

@tag_router.patch("/{tag_id}", response_model=TagResponse)
def update(
    tag_id: int,
    tag: TagUpdate,
    service: TagService = Depends(get_tag_service)
):
    return service.update(tag_id=tag_id, new_name=tag.name)