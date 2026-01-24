# Design Doc


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
| Component | Technology | Version |
| --------- | ---------- | ------- |
| Framework | FastAPI    | 0.128.0 |

### Database
| Component | Technology | Version |
| --------- | ---------- | ------- |
| Database  | PostgreSQL | 16.11   |


## 5. Database Schema

### article Table
| Column      | Type                     |  Constraints                        | Description         |
| ----------- | ------------------------ | ----------------------------------- | ------------------- |
| id          | INTEGER      　          | PK                                  | Article id          |
| title       | VARCHAR(300)             | NOT NULL                            | Article title       |
| title_lower | VARCHAR(300)             | NOT NULL                            | Article title lower |
| url         | VARCHAR(2083)            | NOT NULL                            | Article URL         |
| created_at  | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Creation time       |
| updated_at  | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Last updated time   |
| is_deleted  | BOOLEAN                  | NOT NULL, DEFAULT FALSE             | Soft delete flag    |
| deleted_at  | TIMESTAMP WITH TIME ZONE | NULL                                | Deletion time       |

### tag Table
|Column      | Type         | Constraints | Description    |
| ---------- | ------------ | ----------- | -------------- |
| id         | INTEGER      | PK          | Tag id         |
| name       | VARCHAR(300) | NOT NULL    | Tag name       |
| name_lower | VARCHAR(300) | NOT NULL    | Tag name lower |

### article_tag Table
|Column      | Type     | Constraints | Description |
| ---------- | -------- | ----------- | ----------- |
| article_id | INTEGER  | PK, FK      | article.id  |
| tag_id     | INTEGER  | PK, FK      | tag.id      |


## 6. API Design