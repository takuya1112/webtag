from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models import Tag


class TagRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, tag_id: int) -> Tag | None:
        return self.session.get(Tag, tag_id)
    
    def get_all(self) -> list[Tag]:
        return (
            self.session
            .query(Tag)
            .order_by(func.lower(Tag.name).asc())
            .all() 
        ) 
    
    def search(self, keywords: list[str]) -> list[Tag]:
        conditions = [
            func.lower(Tag.name).like(f"%{keyword}%") 
            for keyword in keywords
        ]

        return (
            self.session
            .query(Tag)
            .filter(*conditions)
            .order_by(func.lower(Tag.name).asc())
            .all()
        )

    def add(self, tag: Tag) -> None:
        self.session.add(tag)
        self.session.flush()

    def hard_delete(self, tag: Tag) -> None:
        self.session.delete(tag)

    def hard_delete_all(self) -> None:
        self.session.query(Tag).delete()

    def update(self, tag: Tag, new_name: str) -> None:
        tag.name = new_name
        self.session.flush()