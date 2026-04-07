from uuid import UUID

from shared.domain.exceptions import InvalidUuidError
from shared.domain.value_objects import AppUuid

from ..exceptions import ArticleIdInvalidError


class ArticleId(AppUuid):
    def __init__(self, value: UUID | str):
        try:
            super().__init__(value)
        except InvalidUuidError:
            raise ArticleIdInvalidError() from None
