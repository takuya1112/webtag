from sqlalchemy.orm import Session
from ..models import Tag
from ..repositories import TagRepository


class TagService:
    def __init__(self, session: Session):
        self.repo = TagRepository(session)

    def get_tag_or_raise(self, tag_id: int) -> Tag:
        tag = self.repo.get(tag_id)
        if not tag:
            raise ValueError(f"Tag with id {tag_id} not found")
        return tag
    
    def normalize(self, name: str) -> str:
        return name.lower().strip()
        
    def create(self, name: str) -> Tag:
        normalized_name = self.normalize(name)
        new_tag = Tag(name=name, normalized_name=normalized_name)
        self.repo.add(new_tag)
        return new_tag

    def delete(self, tag_id: int) -> Tag:
        tag = self.get_tag_or_raise(tag_id)
        self.repo.delete(tag)
        return tag
    
    def delete_all(self) -> int:
        count = self.repo.delete_all()
        return count
    
    def read(self, tag_id: int) -> Tag:
        tag = self.get_tag_or_raise(tag_id)
        return tag

    def read_all(self) -> list[Tag]:
        tags = self.repo.get_all()
        return tags

    def update(self, tag_id: int, new_name: str) -> Tag:
        normalized_name = self.normalize(new_name)
        tag = self.get_tag_or_raise(tag_id)
        self.repo.update(tag, new_name, normalized_name)
        return tag