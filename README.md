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
- Restore deleted article
- Restore all deleted articles
- Hard delete deleted article
- Hard delete all deleted articles
- Get deleted article
- Get all deleted articles

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
├── .devcontainer
│   ├── devcontainer.json
│   └── docker-compose.yml
├── .gitignore
├── README.md
├── backend
│   ├── __init__.py
│   ├── README.md
│   ├── Dockerfile
│   ├── requirements-dev.in
│   ├── requirements-dev.txt
│   ├── requirements.in
│   ├── requirements.txt
│   ├── main.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logging.py
│   ├── startup
│   │   ├── __init__.py
│   │   └── exception_handlers.py
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   ├── endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   ├── login.py
│   │   │   │   ├── logout.py
│   │   │   │   └── signup.py
│   │   │   └── schemas
│   │   │       ├── __init__.py
│   │   │       ├── fields.py
│   │   │       └── validator.py
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── exceptions.py
│   │   │   ├── get_current_user.py
│   │   │   ├── login.py
│   │   │   ├── logout.py
│   │   │   └── signup.py
│   │   └── exceptions
│   │       ├── __init__.py
│   │       └── http.py
│   ├── access_token
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── dependencies.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── exceptions.py
│   │   │   └── jwt_service.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       ├── exceptions.py
│   │       └── jwt_service.py
│   ├── refresh_token
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   ├── endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   └── refresh.py
│   │   │   └── schemas
│   │   │       ├── __init__.py
│   │   │       └── schemas.py
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── create.py
│   │   │   ├── exceptions.py
│   │   │   └── refresh.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── entity.py
│   │   │   ├── exceptions.py
│   │   │   ├── factory.py
│   │   │   ├── refresh_token_generator.py
│   │   │   ├── refresh_token_hasher.py
│   │   │   ├── repository.py
│   │   │   └── value_objects
│   │   │       ├── __init__.py
│   │   │       ├── refresh_token_hash.py
│   │   │       └── refresh_token_id.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       ├── exceptions.py
│   │       ├── model.py
│   │       ├── refresh_token_generator.py
│   │       ├── refresh_token_hasher.py
│   │       └── repository.py
│   │── user
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   ├── error_messages.py
│   │   │   ├── exception_handlers.py
│   │   │   └── handlers.py
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── create.py
│   │   │   └── exceptions.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── entity.py
│   │   │   ├── exceptions.py
│   │   │   ├── factory.py
│   │   │   ├── password_hasher.py
│   │   │   ├── repository.py
│   │   │   └── value_objects
│   │   │       ├── __init__.py
│   │   │       ├── created_at.py
│   │   │       ├── deactivated_at.py
│   │   │       ├── email.py
│   │   │       ├── hashed_password.py
│   │   │       ├── updated_at.py
│   │   │       ├── user_id.py
│   │   │       └── user_name.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │      ├── exceptions.py
│   │       ├── model.py
│   │       ├── password_hasher.py
│   │       └── repository.py
│   ├── article
│   │   ├── __init__.py
│   │   ├── api
│   │   │   └── __init__.py
│   │   ├── application
│   │   │   └── __init__.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── article_entity.py
│   │   │   └── value_objects
│   │   │       ├── __init__.py
│   │   │       ├── article_id.py
│   │   │       ├── article_title.py
│   │   │       └── url.py
│   │   ├── exceptions
│   │   │   ├── __init__.py
│   │   │   └── domain.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       ├── article_model.py
│   │       └── article_tag_model.py
│   ├── tag
│   │   ├── __init__.py
│   │   ├── api
│   │   │   └── __init__.py
│   │   ├── application
│   │   │   └── __init__.py
│   │   ├── domain
│   │   │   └── __init__.py
│   │   ├── exceptions.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       └── model.py
│   ├── shared
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── dependencies.py
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── exceptions.py
│   │   │   ├── retry.py
│   │   │   └── uow.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── clock.py
│   │   │   ├── exceptions.py
│   │   │   ├── id_generator.py
│   │   │   └── value_objects
│   │   │       ├── __init__.py
│   │   │       ├── app_uuid.py
│   │   │       └── aware_datetime.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       ├── base.py
│   │       ├── clock.py
│   │       ├── engine.py
│   │       ├── exceptions.py
│   │       ├── id_generator.py
│   │       ├── session.py
│   │       └── uow.py
│   ├── alembic.ini
│   ├── migrations
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 813696133fe4_initial.py
│   ├── pytest.toml
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── e2e
│       │   └── __init__.py
│       ├── integration
│       │   └── __init__.py
│       └── unit
│           ├── __init__.py
│           ├── conftest.py
│           ├── shared
│           │   ├── __init__.py
│           │   ├── conftest.py
│           │   ├── domain
│           │   │   ├── __init__.py
│           │   │   └── test_value_objects.py
│           │   └── fakes
│           │       ├── __init__.py
│           │       ├── clock.py
│           │       ├── id_generator.py
│           │       ├── password_hasher.py
│           │       └── uow.py
│           └── user
│               ├── __init__.py
│               ├── application
│               │   ├── __init__.py
│               │   └── test_create.py
│               ├── conftest.py
│               ├── domain
│               │   ├── __init__.py
│               │   ├── test_entity.py
│               │   ├── test_factory.py
│               │   └── test_value_objects.py
│               └── fakes
│                   ├── __init__.py
│                   └── repository.py
├── docker-compose.yml
├── docs
│   ├── assets
│   │   └── ER diagram.drawio.png
│   └── design.md
└── frontend
    ├── README.md
    ├── eslint.config.js
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── public
    │   └── vite.svg
    ├── src
    │   ├── App.css
    │   ├── App.tsx
    │   ├── assets
    │   │   └── react.svg
    │   ├── index.css
    │   └── main.tsx
    ├── tsconfig.app.json
    ├── tsconfig.json
    ├── tsconfig.node.json
    └── vite.config.ts
```
