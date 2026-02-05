from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..db.core import get_session
from ..db.services import TagService
from ..schemas.tag import TagCreate, TagUpdate, TagResponse


router = APIRouter(
    prefix="/tags",
    tags=["Tag"]
)

def get_tag_service(
        session: Session = Depends(get_session)
        ) -> TagService:
    return TagService(session)

@router.post("/", response_model=TagResponse, status_code=201)
def post(
    tag: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    return service.create(tag)

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
def get(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    return service.get_tag_or_raise(tag_id)

@router.get("/", response_model=list[TagResponse])
def get_all(
    q: list[str] = Query(default=[]),
    service: TagService = Depends(get_tag_service)
):
    return service.read_all(q)

@router.patch("/{tag_id}", response_model=TagResponse)
def update(
    tag_id: int,
    tag: TagUpdate,
    service: TagService = Depends(get_tag_service)
):
    return service.update(tag_id=tag_id, new_name=tag.name)