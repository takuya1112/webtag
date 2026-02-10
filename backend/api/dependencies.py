from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from db.models import User
from db import get_session
from core.security import decode_access_token
from services import (
    UserService, ArticleService, DeletedArticleService,
    TagService, ArticleTagService,
)

"""
Dependency providers for FastAPI.
"""

SessionDep = Annotated[Session, Depends(get_session)]

def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

def get_article_service(session: SessionDep) -> ArticleService:
    return ArticleService(session)

ArticleServiceDep = Annotated[ArticleService, Depends(get_article_service)]


def get_deleted_article_service(session: SessionDep) -> DeletedArticleService:
    return DeletedArticleService(session)

DeletedArticleServiceDep = Annotated[
    DeletedArticleService, 
    Depends(get_deleted_article_service),
]


def get_tag_service(session: SessionDep) -> TagService:
    return TagService(session)

TagServiceDep = Annotated[TagService, Depends(get_tag_service)]


def get_article_tag_service(session: SessionDep) -> ArticleTagService:
    return ArticleTagService(session)

ArticleTagServiceDep = Annotated[
    ArticleTagService, 
    Depends(get_article_tag_service),
] 

security = HTTPBearer()

def get_current_user( 
    service: UserServiceDep,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],  
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise credentials_exception
    
    public_id = payload.get("sub")
    if public_id is None:
        raise credentials_exception
    
    user = service.repo.get_by_public_id(public_id)
    if user is None:
        raise credentials_exception
    
    return user

CurrentUserDep = Annotated[User, Depends(get_current_user)]