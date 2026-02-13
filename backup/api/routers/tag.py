from fastapi import APIRouter, Query
from ..dependencies import TagServiceDep
from schemas.tag import TagCreate, TagUpdate, TagResponse


router = APIRouter(
    prefix="/tags",
    tags=["Tag"],
)

@router.post("/", response_model=TagResponse, status_code=201)
def post(
    service: TagServiceDep,
    tag: TagCreate,
):
    return service.create(tag)

@router.delete("/{tag_id}", status_code=204)
def hard_delete(
    service: TagServiceDep,
    tag_id: int,
):
    service.hard_delete(tag_id)

@router.delete("/", status_code=204)
def hard_delete_all(
    service: TagServiceDep,
):
    service.hard_delete_all()

@router.get("/{tag_id}", response_model=TagResponse)
def get(
    service: TagServiceDep,
    tag_id: int,
):
    return service.get_tag_or_raise(tag_id)

@router.get("/", response_model=list[TagResponse])
def get_all(
    service: TagServiceDep,
    q: list[str] = Query(default=[]),
):
    return service.read_all(q)

@router.patch("/{tag_id}", response_model=TagResponse)
def update(
    service: TagServiceDep,
    tag_id: int,
    tag: TagUpdate,
):
    return service.update(tag_id=tag_id, new_name=tag.name)