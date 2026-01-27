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
- Rename article
- Update article URL
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

### Database
- **PostgreSQL**

## 5. Structure
```
.
├── README.md
├── alembic.ini
├── backend
│   └── db
│       ├── config.py
│       ├── crud
│       │   ├── article.py
│       │   ├── deleted_article.py
│       │   └── tag.py
│       ├── database.py
│       └── models
│           ├── article.py
│           ├── article_tag.py
│           └── tag.py
├── docs
│   ├── ER diagram.png
│   └── design.md
└── main.py
```