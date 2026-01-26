from sqlalchemy.orm import Session
from ..models import TagAlias
from ..repositories import TagAliasRepository


class TagAliasService:
    def __init__(self, session: Session):
        self.repo = TagAliasRepository(session)

    def normalize(self, tag_alias_name: str) -> TagAlias:
        nomalized = tag_alias_name.lower()
        alias = self.repo.get_alias_by_name(nomalized)

        if alias:
            return alias
        
        alias = TagAlias(name=nomalized)
        self.repo.add(alias)
        return alias

    def delete(self, tag_alias_id: int) -> TagAlias:
        alias = self.repo.get_alias_or_raise(tag_alias_id)
        self.repo.delete(alias)
        return alias

    def delete_all(self) -> int:
        return self.repo.delete_all()