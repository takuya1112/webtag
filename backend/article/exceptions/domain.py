class ArticleDomainError(Exception):
    pass


class ArticleAlreadyDeleted(ArticleDomainError):
    pass


class ArticleNotDeleted(ArticleDomainError):
    pass
