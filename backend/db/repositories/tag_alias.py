from sqlalchemy.orm import Session
from ..models import TagAlias


class TagAliasRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_alias_or_raise(self, tag_alias_id: int) -> TagAlias:
        alias = self.session.get(TagAlias, tag_alias_id)
        if not alias:
            raise ValueError(f"Tag Alias  with id {tag_alias_id} not found")
        return alias
    
    def get_all(self) -> list[TagAlias]:
        tag_alias = self.session.query(TagAlias).all()
        return tag_alias
    
    def get_alias_by_name(self, tag_alias_name: str) -> TagAlias | None:
        return (
            self.session.query(TagAlias)
            .filter(TagAlias.name == tag_alias_name)
            .one_or_none()
        )
    
    def add(self, tag_alias_name: TagAlias) -> None:
        self.session.add(tag_alias_name)
        self.session.flush()

    def delete(self, tag_alias: TagAlias) -> None:
        self.session.delete(tag_alias)
        self.session.flush()

    def delete_all(self) -> int:
        count = self.session.query(TagAlias).delete()
        self.session.flush()
        return count