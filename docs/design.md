# WebTag 設計書

## 1.データ設計

### エンティティ一覧

### article
|カラム名        | 型　     　| 制約      | 説明  　      |
| ------------- | ---------- | -------- | ------------  |
| article_id    | INT      　| PK       | 記事のID      |
| article_title | VARCHAR  　| NOT NULL | 記事のタイトル |
| article_link  | VARCHAR  　| NOT NULL | 記事のリンク   |
| created_at    | TIMESTAMP | NOT NULL  | 作成日時      |
| edited_at     | TIMESTAMP | NOT NULL  | 編集日時      |

### tag
|カラム名   | 型      | 制約     | 説明       |
| -------- | ------- | -------- | --------- |
| tag_id   | INT     | PK       | タグのID   |
| tag_name | VARCHAR | NOT NULL | タグの名前 |

### article_tag
|カラム名     | 型  |　制約  |　説明　             |
| ---------- | --- | ------ | ------------------ |
| article_id | INT | PK, FK | article.article_id |
| tag_id     | INT | PK, FK | tag.tag_id         |

## 説明
Article と Tag は多対多関係である。
しかし、SQLでは、1カラムの中にデータは１つずつしか入れないという前提があるので、
ArticleTag を中間テーブルとして採用することで、この問題を解消しました。