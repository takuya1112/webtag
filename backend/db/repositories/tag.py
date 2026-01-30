from sqlalchemy.orm import Session
from ..models import Tag


class TagRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, tag_id: int) -> Tag | None:
        return self.session.get(Tag, tag_id)
    
    def get_all(self) -> list[Tag]:
        return self.session.query(Tag).all()

    def add(self, tag: Tag) -> None:
        self.session.add(tag)
        self.session.flush()

    def hard_delete(self, tag: Tag) -> None:
        self.session.delete(tag)
        self.session.flush()

    def hard_delete_all(self) -> None:
        self.session.query(Tag).delete()
        self.session.flush()

    def update(self, tag: Tag, new_name: str, normalized_name: str) -> None:
        tag.name = new_name
        tag.normalized_name = normalized_name
        self.session.flush()