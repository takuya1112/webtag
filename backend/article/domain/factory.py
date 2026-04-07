from shared.domain.clock import Clock
from shared.domain.id_generator import IdGenerator
from user.domain.value_objects import UserId

from .entity import ArticleEntity
from .value_objects import URL, ArticleId, ArticleTitle, CreatedAt, UpdatedAt


class ArticleFactory:
    def __init__(self, id_generator: IdGenerator, clock: Clock) -> None:
        self.id_generator = id_generator
        self.clock = clock

    def create(
        self,
        user_id: UserId,
        title: ArticleTitle,
        url: URL,
    ) -> ArticleEntity:
        id = ArticleId(self.id_generator.generate())
        now = self.clock.now()

        return ArticleEntity(
            id=id,
            user_id=user_id,
            title=title,
            url=url,
            created_at=CreatedAt(now),
            updated_at=UpdatedAt(now),
            deleted_at=None,
        )
