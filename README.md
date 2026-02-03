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
- Get article
- Get all articles
- Update article

### Tag Management

- Create tag
- Hard delete tag
- Hard delete all tags
- Get tag
- Get all tags
- Update tag
- Attach tag to the article
- Remove tag from the article
- Get tags attached to the article

### Deleted Article Management

- Restore deleted article
- Restore all deleted articles
- Hard delete deleted article
- Hard delete all deleted articles
- Get deleted article
- Get all deleted articles

## 4. Tech Stack

### Frontend

- **TypeScript**
- **React**
- **Vite**

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
├── .gitignore
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
│   │   │   ├── article_tag.py
│   │   │   ├── deleted_article.py
│   │   │   └── tag.py
│   │   └── services
│   │       ├── article.py
│   │       ├── article_tag.py
│   │       ├── deleted_article.py
│   │       └── tag.py
│   ├── routers
│   │   ├── article.py
│   │   ├── article_tag.py
│   │   ├── deleted_article.py
│   │   └── tag.py
│   └── schemas
│       ├── article.py
│       ├── article_tag.py
│       └── tag.py
├── docs
│   ├── ER diagram.drawio.png
│   └── design.md
├── frontend
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   └── vite.svg
│   ├── src
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── index.css
│   │   └── main.tsx
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
└── main.py
```
