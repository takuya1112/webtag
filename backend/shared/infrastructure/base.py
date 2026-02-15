from sqlalchemy.orm import declarative_base

Base = declarative_base()


def load_all_models():
    from article.infrastructure.article_model import ArticleModel  # noqa
    from article.infrastructure.article_tag_model import ArticleTagModel  # noqa
    from refresh_token.infrastructure.model import RefreshTokenModel  # noqa
    from tag.infrastructure.model import TagModel  # noqa
    from user.infrastructure.model import UserModel  # noqa
