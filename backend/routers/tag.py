from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import TagService
from ..schemas.tag import (
    TagCreate,
    TagUpdate,
    TagResponse
)

router = APIRouter(
    prefix="/tags",
    tags=["Tag"]
)

def get_tag_service(
        session: Session = Depends(get_session)
        ) -> TagService:
    return TagService(session)

@router.post("/", response_model=TagResponse, status_code=201)
def create(
    tag: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    return service.create(name=tag.name)

@router.delete("/{tag_id}", status_code=204)
def hard_delete(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    service.hard_delete(tag_id)

@router.delete("/", status_code=204)
def hard_delete_all(
    service: TagService = Depends(get_tag_service)
):
    service.hard_delete_all()

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

@router.patch("/{tag_id}", response_model=TagResponse)
def update(
    tag_id: int,
    tag: TagUpdate,
    service: TagService = Depends(get_tag_service)
):
    return service.update(tag_id=tag_id, new_name=tag.name)