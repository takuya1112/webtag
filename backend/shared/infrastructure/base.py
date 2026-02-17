from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

naming_convention = {
    "ix": "ix_%(table_name)s_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=naming_convention)


def load_all_models():
    from article.infrastructure.article_model import ArticleModel  # noqa
    from article.infrastructure.article_tag_model import ArticleTagModel  # noqa
    from refresh_token.infrastructure.model import RefreshTokenModel  # noqa
    from tag.infrastructure.model import TagModel  # noqa
    from user.infrastructure.model import UserModel  # noqa
