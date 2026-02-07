from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.core import get_session
from ..db.services import (
    UserService, ArticleService, DeletedArticleService,
    TagService, ArticleTagService
)

SessionDep = Annotated[Session, Depends(get_session)]

""""""
def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

""""""
def get_article_service(session: SessionDep) -> ArticleService:
    return ArticleService(session)

ArticleServiceDep = Annotated[ArticleService, Depends(get_article_service)]


""""""
def get_deleted_article_service(session: SessionDep) -> DeletedArticleService:
    return DeletedArticleService(session)

DeletedArticleServiceDep = Annotated[DeletedArticleService, Depends(get_deleted_article_service)]


""""""
def get_tag_service(session: SessionDep) -> TagService:
    return TagService(session)

TagServiceDep = Annotated[TagService, Depends(get_tag_service)]


""""""
def get_article_tag_service(session: SessionDep) -> ArticleTagService:
    return ArticleTagService(session)

ArticleTagServiceDep = Annotated[ArticleTagService, Depends(get_article_tag_service)] 