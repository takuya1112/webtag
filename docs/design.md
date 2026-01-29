# Design Doc

<!--
TODO
１. searchの計算量問題
***必要ならデータ構造の変更***

2. dogstring や README 等の書き物を完成させる

3. API 設計

4. repositories での fluch() 多用問題、
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
| Column           | Type                     |  Constraints                        | Description              |
| ---------------- | ------------------------ | ----------------------------------- | ------------------------ |
| id               | INTEGER      　          | PK                                  | Article id               |
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
| Column     | Type     | Constraints | Description |
| ---------- | -------- | ----------- | ----------- |
| article_id | INTEGER  | PK, FK      | article.id  |
| tag_id     | INTEGER  | PK, FK      | tag.id      |


## 6. API Design

| Endpoint       | Method | Request Body  | Response Body         | Status Code | Description              |
| -------------- | ------ | ------------- | --------------------- | ----------- | ------------------------ |
| /articles      | POST   | ArticleCreate | ArticleResponse       | 201 / 400   | Create article           |
| /articles/{id} | DELETE | None          | None                  | 204 / 404   | Soft delete an article   |
| /articles      | DELETE | None          | None                  | 204         | Soft delete all articles |
| /articles/{id} | GET    | None          | ArticleResponse       | 200 / 404   | Get article              |
| /articles      | GET    | None          | List[ArticleResponse] | 200         | Get all articles         |
| /articles/{id} | PATCH  | ArticleUpdate | ArticleResponse       | 200 / 404   | Update article           |

### Error Responses
- 400: title or url are empty
- 404: Resource not found