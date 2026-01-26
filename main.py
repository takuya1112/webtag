from backend.db import get_session
from backend.db.services import article
from backend.db.services import deleted_article
from backend.db.services import tag

with get_session() as session:
    with session.begin():
        a = tag.TagService(session)
        print(a.update(7, "take"))
        
