# WebTag

## 1. Description

WebTag is an application that allows you to tag websites you want to revisit later,
and find them easily and quickly.

## 2. Purpose

The goal of this project is to keep the bookmarks bar and the desktop clean by removing excessive shortcut icons
and to make it easier to find the websites you need.

## 3. Features

### Article Management

- Create article
- Soft delete article
- Soft delete all articles
- View article
- List all articles
- Update article
- Search articles

### Tag Management

- Create tag
- Hard delete tag
- Hard delete all tags
- View tag
- List all tags
- Update tag
- Attach tag to article
- Remove tag from article

### Deleted Article Management

- View deleted article
- List all deleted articles
- Hard delete deleted article
- Hard delete all deleted articles
- Restore deleted article
- Restore all deleted articles

## 4. Tech Stack

### Backend

- **Python**
- **SQLAlchemy**
- **Alembic**

### API

- **FastAPI**
- **pydantic**

### Database

- **PostgreSQL**

## 5. Structure

```
.
├── README.md
├── alembic.ini
├── backend
│   ├── db
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models
│   │   │   ├── article.py
│   │   │   ├── article_tag.py
│   │   │   ├── tag.py
│   │   │   └── user.py
│   │   ├── repositories
│   │   │   ├── article.py
│   │   │   ├── article_search.py
│   │   │   ├── article_tag.py
│   │   │   ├── deleted_article.py
│   │   │   └── tag.py
│   │   └── services
│   │       ├── article.py
│   │       ├── article_search.py
│   │       ├── article_tag.py
│   │       ├── deleted_article.py
│   │       └── tag.py
│   ├── routers
│   │   ├── article.py
│   │   ├── article_search.py
│   │   ├── article_tag.py
│   │   ├── deleted_article.py
│   │   └── tag.py
│   └── schemas
│       ├── article.py
│       └── article_tag.py
├── docs
│   ├── ER diagram.drawio.png
│   └── design.md
├── frontend
└── main.py

```
