# from backend.db import get_session
# from backend.db.services import *

# with get_session() as session:
#     with session.begin():
#         a = ArticleSearchService(session)
#         print(a.search(["woman"]))
        

# from fastapi import FastAPI
# from backend.routers import *

# app = FastAPI()
# app.include_router(deleted_article.router)


import bcrypt
pw = b'!!eC87!$7^oZ6L'
s = bcrypt.gensalt()
h = bcrypt.hashpw(pw, s) # Hash password
entered_pw = b'!!eC87!$7^oZ6L'

print(s)
print(h)

if bcrypt.checkpw(entered_pw, h):
    print("Password match!")
else:
    print("Incorrect password.")