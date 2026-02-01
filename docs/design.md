# Design Doc

<!--
TODO
１. searchの計算量問題
***必要ならデータ構造の変更***

2. dogstring や README 等の書き物を完成させる

4. repositories での fluch() 多用問題、

5. None.strip() エラー問題

6. ?sort= 機能の追加

-->

## 1. Context

## 2. Goals

## 3. Non-Goals

## 4. Tech Stack

### Backend

| Component | Technology | Version |
| --------- | ---------- | ------- |
| Language  | Python     | 3.12.3  |
| ORM       | SQLAlchemy | 2.0.45  |
| Migration | Alembic    | 1.18.1  |

### API

| Component       | Technology | Version |
| --------------- | ---------- | ------- |
| Framework       | FastAPI    | 0.128.0 |
| Data Validation | Pydantic   | 2.12.5  |

### Database

| Component | Technology | Version |
| --------- | ---------- | ------- |
| Database  | PostgreSQL | 16.11   |

## 5. Database Schema

### article Table

| Column           | Type                     | Constraints                         | Description              |
| ---------------- | ------------------------ | ----------------------------------- | ------------------------ |
| id               | INTEGER 　               | PK                                  | Article id               |
| title            | VARCHAR(300)             | NOT NULL                            | Article title            |
| normalized_title | VARCHAR(300)             | NOT NULL                            | Article normalized title |
| url              | VARCHAR(2083)            | NOT NULL                            | Article URL              |
| created_at       | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Creation time            |
| updated_at       | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Last updated time        |
| is_deleted       | BOOLEAN                  | NOT NULL, DEFAULT FALSE             | Soft delete flag         |
| deleted_at       | TIMESTAMP WITH TIME ZONE | NULL                                | Deletion time            |

### tag Table

| Column          | Type         | Constraints | Description         |
| --------------- | ------------ | ----------- | ------------------- |
| id              | INTEGER      | PK          | Tag id              |
| name            | VARCHAR(300) | NOT NULL    | Tag name            |
| normalized_name | VARCHAR(300) | NOT NULL    | Tag normalized name |

### article_tag Table

| Column     | Type    | Constraints | Description |
| ---------- | ------- | ----------- | ----------- |
| article_id | INTEGER | PK, FK      | article.id  |
| tag_id     | INTEGER | PK, FK      | tag.id      |

## 6. API Design

| Endpoint                             | Method | Request Body  | Response Body         | Status Code | Description                      | X   |
| ------------------------------------ | ------ | ------------- | --------------------- | ----------- | -------------------------------- | --- |
| /articles                            | POST   | ArticleCreate | ArticleResponse       | 201/422     | Create article                   | X   |
| /articles/{id}                       | DELETE | None          | None                  | 204/404     | Soft delete article              | X   |
| /articles                            | DELETE | None          | None                  | 204         | Soft delete all articles         | X   |
| /articles/{id}                       | GET    | None          | ArticleResponse       | 200/404     | Get article                      | X   |
| /articles                            | GET    | None          | list[ArticleResponse] | 200         | Get all articles                 | X   |
| /articles/{id}                       | PATCH  | ArticleUpdate | ArticleResponse       | 200/400/404 | Update article                   |     |
| /articles/search                     | GET    | None          | list[ArticleResponse] | 200         | Search articles                  |     |
| /articles/deleted/{id}               | DELETE | None          | None                  | 204/404/409 | Hard delete article              | X   |
| /articles/deleted                    | DELETE | None          | None                  | 204         | Hard delete all articles         | X   |
| /articles/deleted/{id}               | GET    | None          | ArticleResponse       | 200/404/409 | Get deleted article              | X   |
| /articles/deleted                    | GET    | None          | list[ArticleResponse] | 200         | Get all deleted articles         | X   |
| /articles/deleted/{id}               | PATCH  | None          | ArticleResponse       | 200/404/409 | Restore article                  |     |
| /articles/deleted                    | PATCH  | None          | RestoreAllResponse    | 200         | Restore all deleted articles     |     |
| /tags                                | POST   | TagCreate     | TagResponse           | 201/400     | Create tag                       |     |
| /tags/{id}                           | DELETE | None          | None                  | 204/404     | Hard delete tag                  |     |
| /tags                                | DELETE | None          | None                  | 204         | Hard delete all tags             |     |
| /tags/{id}                           | GET    | None          | TagResponse           | 200/404     | Get tag                          |     |
| /tags                                | GET    | None          | list[TagResponse]     | 200         | Get all tags                     |     |
| /tags/{id}                           | PATCH  | TagUpdate     | TagResponse           | 200/400/404 | Update tag                       |     |
| /articles/{article_id}/tags          | GET    | None          | list[TagResponse]     | 200/404     | Get tags attached to the article | X   |
| /articles/{article_id}/tags/{tag_id} | POST   | None          | ArticleTagResponse    | 201/404/409 | attach tag to the article        | X   |
| /articles/{article_id}/tags/{tag_id} | DELETE | None          | None                  | 204/404     | remove tag from the article      | X   |

### Error Responses

- 400: Invalid request
- 404: Resource not found
- 409: Conflict
- 422: Validation Error
