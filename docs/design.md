# WebTag 設計書

## 1.データ設計

### エンティティ一覧

### article
|カラム名     | 型　     　   | 制約                                 | 説明  　      |
| ---------- | ------------- | ----------------------------------- | ------------  |
| id         | INT      　   | PK                                  | 記事のID       |
| title      | VARCHAR(300)  | NOT NULL                            | 記事のタイトル |
| url        | VARCHAR(2083) | NOT NULL                            | 記事のURL      |
| created_at | TIMESTAMP     | NOT NULL, DEFAULT CURRENT_TIMESTAMP | 作成日時      |
| edited_at  | TIMESTAMP     | NOT NULL, DEFAULT CURRENT_TIMESTAMP | 編集日時      |
| is_deleted | BOOLEAN       | NOT NULL, DEFAULT FALSE             | 論理削除フラグ |
| deleted_at | TIMESTAMP     | NULL                                | 削除日時      |

### tag
|カラム名 | 型           | 制約     | 説明       |
| ------ | ------------ | -------- | --------- |
| id     | INT          | PK       | タグのID   |
| name   | VARCHAR(300) | NOT NULL | タグの名前 |

### article_tag
|カラム名     | 型  |　制約  |　説明　     |
| ---------- | --- | ------ | ---------- |
| article_id | INT | PK, FK | article.id |
| tag_id     | INT | PK, FK | tag.id     |

## 説明
Article と Tag は多対多関係である。
しかし、SQLでは、1カラムの中にデータは１つずつしか入れないという前提があるので、
ArticleTag を中間テーブルとして採用することで、この問題を解消しました。