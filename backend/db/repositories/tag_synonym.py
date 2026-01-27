from sqlalchemy.orm import Session
from ..models import TagSynonym


class TagSynonymRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_synonym_or_raise(self, synonym_id: int) -> TagSynonym:
        synonym = self.session.get(TagSynonym, synonym_id)
        if not synonym:
            raise ValueError(f"Tag Alias  with id {synonym_id} not found")
        return synonym
    
    def get_all(self) -> list[TagSynonym]:
        synonyms = self.session.query(TagSynonym).all()
        return synonyms
    
    def get_synony_by_name(self, synonym_name: str) -> TagSynonym | None:
        return (
            self.session.query(TagSynonym)
            .filter(TagSynonym.name == synonym_name)
            .one_or_none()
        )
    
    def add(self, synonym_name: TagSynonym) -> None:
        self.session.add(synonym_name)
        self.session.flush()

    def delete(self, synonym: TagSynonym) -> None:
        self.session.delete(synonym)
        self.session.flush()

    def delete_all(self) -> int:
        count = self.session.query(TagSynonym).delete()
        self.session.flush()
        return count