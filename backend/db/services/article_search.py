from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import ArticleSearchRepository

class ArticleSearchService:
    BOTH_MATCHED = 30
    TAG_ONLY_MATCHED = 20
    TITLE_ONLY_MATCHED = 10

    TAG_MATCH_SCORE = 10
    TITLE_MATCH_SCORE = 5

    KEYWORD_LENGTH = 2

    def __init__(self, session: Session):
        self.repo = ArticleSearchRepository(session)

    def calculate_score(self, article: Article, keywords: list[str]) -> int:
            score = 0

            article_tags = {tag.normalized_name for tag in article.tags}
            tag_match = sum(1 for keyword in keywords if keyword in article_tags)

            title_match = sum(1 for keyword in keywords if keyword in article.normalized_title)

            if tag_match > 0 and title_match > 0:
                score += self.BOTH_MATCHED
            elif tag_match > 0:
                score += self.TAG_ONLY_MATCHED
            elif title_match > 0:
                score += self.TITLE_ONLY_MATCHED

            score += tag_match * self.TAG_MATCH_SCORE + title_match * self.TITLE_MATCH_SCORE
            
            return score 


    def search(self,  keywords: list[str]) -> list[Article]:
        if not keywords:
            return []
        
        valid_keyword = [keyword.lower().strip() for keyword in keywords
                          if len(keyword) > self.KEYWORD_LENGTH]
        valid_keyword = list(set(valid_keyword))

        if not valid_keyword:
             return []

        articles = self.repo.search_candidate(valid_keyword)
        articles_with_score = [(self.calculate_score(article, valid_keyword), article) for article in articles]
        articles_with_score.sort(key=lambda x: (x[0], x[1].created_at), reverse=True)
        return [article for _, article in articles_with_score]
