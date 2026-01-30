from sqlalchemy.orm import Session
from ..models import Tag
from ..repositories import TagRepository
from fastapi import HTTPException, status


class TagService:
    def __init__(self, session: Session):
        self.repo = TagRepository(session)

    def get_tag_or_raise(self, tag_id: int) -> Tag:
        tag = self.repo.get(tag_id)
        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tag not found"
            )
        return tag
    
    def normalize(self, name: str) -> str:
        if not name.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="name must not be empty"
            )
        return name.lower().strip()
        
    def create(self, name: str) -> Tag:
        normalized_name = self.normalize(name)
        new_tag = Tag(name=name, normalized_name=normalized_name)
        self.repo.add(new_tag)
        return new_tag

    def hard_delete(self, tag_id: int) -> None:
        tag = self.get_tag_or_raise(tag_id)
        self.repo.hard_delete(tag)
    
    def hard_delete_all(self) -> None:
        self.repo.hard_delete_all()
    
    def read(self, tag_id: int) -> Tag:
        return self.get_tag_or_raise(tag_id)

    def read_all(self) -> list[Tag]:
        return self.repo.get_all()

    def update(self, tag_id: int, new_name: str) -> Tag:
        normalized_name = self.normalize(new_name)
        tag = self.get_tag_or_raise(tag_id)
        self.repo.update(tag, new_name, normalized_name)
        return tag