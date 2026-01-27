from sqlalchemy.orm import Session
from ..models import Tag
from .tag_synonym import TagSynonymService
from ..repositories import TagRepository


class TagService:
    def __init__(self, session: Session):
        self.repo = TagRepository(session)
        self.synonym_service = TagSynonymService(session)

    def get_tag_or_raise(self, tag_id: int) -> Tag:
        tag = self.repo.get(tag_id)
        if not tag:
            raise ValueError(f"Tag with id {tag_id} not found")
        return tag
    
    def delete_synonym_if_unused(self, synonym_id: int):
        if not self.repo.exists_by_alias_id(synonym_id):
            self.synonym_service.delete(synonym_id)
        
    def create(self, name: str) -> Tag:
        synonym = self.synonym_service.normalize(name)
        new_tag = Tag(name=name, synonym_id=synonym.id)
        self.repo.add(new_tag)
        return new_tag

    def delete(self, tag_id: int) -> None:
        tag = self.get_tag_or_raise(tag_id)
        synonym = tag.synonym
        self.repo.delete(tag)
        self.delete_synonym_if_unused(synonym.id)
    
    def delete_all(self) -> tuple[int, int]:
        tag_count = self.repo.delete_all()
        synonym_count = self.synonym_service.delete_all()
        return tag_count, synonym_count
    
    def read(self, tag_id: int) -> Tag:
        tag = self.get_tag_or_raise(tag_id)
        return tag

    def read_all(self) -> list[Tag]:
        tags = self.repo.get_all()
        return tags

    def update(self, tag_id: int, new_name: str) -> Tag:
        new_synonym = self.synonym_service.normalize(new_name)
        tag = self.get_tag_or_raise(tag_id)
        synonym = tag.synonym
        self.repo.update(tag, new_name, new_synonym.id)
        self.delete_synonym_if_unused(synonym.id)
        return tag