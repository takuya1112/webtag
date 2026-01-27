from sqlalchemy.orm import Session
from ..models import TagSynonym
from ..repositories import TagSynonymRepository


class TagSynonymService:
    def __init__(self, session: Session):
        self.repo = TagSynonymRepository(session)

    def normalize(self, synonym_name: str) -> TagSynonym:
        nomalized = synonym_name.lower()
        synonym = self.repo.get_synony_by_name(nomalized)

        if synonym:
            return synonym
        
        synonym = TagSynonym(name=nomalized)
        self.repo.add(synonym)
        return synonym

    def delete(self, synonym_id: int) -> TagSynonym:
        synonym = self.repo.get_synonym_or_raise(synonym_id)
        self.repo.delete(synonym)
        return synonym

    def delete_all(self) -> int:
        return self.repo.delete_all()