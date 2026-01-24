from backend.db import get_session
from backend.db.crud import article
from backend.db.crud import deleted_article
from backend.db.crud import tag

with get_session() as session:
    print(tag.create(session=session, name="TAKU TAKU"))
