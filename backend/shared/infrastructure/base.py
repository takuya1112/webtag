from sqlalchemy.orm import declarative_base

Base = declarative_base()


def load_all_models():
    from refresh_token.infrastructure.model import (
        RefreshTokenModel,  # noqa
    )
