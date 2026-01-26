from sqlalchemy.orm import Session
from ..models import Tag


class TagRepository:
    def __init__(self, session: Session):
        self.session = session

    def exists_by_alias_id(self, alias_id: int) -> bool:
        return (
            self.session
            .query(Tag)
            .filter(Tag.alias_id == alias_id)
            .first()
            is not None
        )

    def get(self, tag_id: int) -> Tag | None:
        return self.session.get(Tag, tag_id)
    
    def get_all(self) -> list[Tag]:
        tags = self.session.query(Tag).all()
        return tags

    def add(self, tag: Tag) -> None:
        self.session.add(tag)
        self.session.flush()

    def delete(self, tag: Tag) -> None:
        self.session.delete(tag)
        self.session.flush()

    def delete_all(self) -> int:
        count = self.session.query(Tag).delete()
        self.session.flush()
        return count

    def update(self, tag: Tag, new_name: str, alias_id: int) -> None:
        tag.name = new_name
        tag.alias_id = alias_id
        self.session.flush()