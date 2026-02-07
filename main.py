# from backend.db import get_session
# from backend.db.services import *

# with get_session() as session:
#     with session.begin():
#         a = ArticleSearchService(session)
#         print(a.search(["woman"]))
        

# from fastapi import FastAPI
# from backend.routers import *

# app = FastAPI()
# app.include_router(user.router)

from sqlalchemy.orm import Session
from backend.db.core.database import SessionLocal 
from backend.db.models import User
from uuid import uuid4

session: Session = SessionLocal()

users = [
    User(
        public_id=uuid4(),
        name=f"user_{i}",
        email=f"user_@example.com",
        password_hash="dummy"
    )
    for i in range(2)
]

session.add_all(users)
session.commit()
session.close()
