from sqlalchemy.orm import Session
from ..models import Tag
from .tag_alias import TagAliasService
from ..repositories import TagRepository


class TagService:
    def __init__(self, session: Session):
        self.repo = TagRepository(session)
        self.alias_service = TagAliasService(session)

    def get_tag_or_raise(self, tag_id: int) -> Tag:
        tag = self.repo.get(tag_id)
        if not tag:
            raise ValueError(f"Tag with id {tag_id} not found")
        return tag
    
    def delete_alias_if_unused(self, alias_id: int):
        if not self.repo.exists_by_alias_id(alias_id):
            self.alias_service.delete(alias_id)
        
    def create(self, name: str) -> Tag:
        alias = self.alias_service.normalize(name)
        new_tag = Tag(name=name, alias_id=alias.id)
        self.repo.add(new_tag)
        return new_tag

    def delete(self, tag_id: int) -> None:
        tag = self.get_tag_or_raise(tag_id)
        alias = tag.alias
        self.repo.delete(tag)
        self.delete_alias_if_unused(alias.id)
    
    def delete_all(self) -> tuple[int, int]:
        tag_count = self.repo.delete_all()
        alias_count = self.alias_service.delete_all()
        return tag_count, alias_count
    
    def read(self, tag_id: int) -> Tag:
        tag = self.get_tag_or_raise(tag_id)
        return tag

    def read_all(self) -> list[Tag]:
        tags = self.repo.get_all()
        return tags

    def update(self, tag_id: int, new_name: str) -> Tag:
        new_alias = self.alias_service.normalize(new_name)
        tag = self.get_tag_or_raise(tag_id)
        alias = tag.alias
        self.repo.update(tag, new_name, new_alias.id)
        self.delete_alias_if_unused(alias.id)
        return tag