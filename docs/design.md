# WebTag 設計書

## 1.データ設計

### エンティティ一覧
Article
-Article ID (PK)
-Title
-Web Link
-Create Data
-Edit Data

Tag
-Tag ID (PK)
-Tag Name

ArticleTag
-Article ID (PK FK)
-Tag ID (PK FK)

## 設計上の判断
Article と Tag は多対多関係である。
しかし、SQLでは、1カラムの中にデータは１つずつしか入れないという前提があるので、
ArticleTag を中間テーブルとして採用しました。