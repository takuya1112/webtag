# WebTag 設計書

## 1.データ設計

### エンティティ一覧

### Article
|カラム名      | 型　     　| 制約      | 説明  　      |
| ----------- | ---------- | -------- | ------------  |
| ID          | INT      　| PK       | 記事のID      |
| Title       | VARCHAR  　| NOT NULL | 記事のタイトル |
| Web Link    | VARCHAR  　| NOT NULL | 記事のリンク   |
| Create Data | TIMESTAMP | NOT NULL  | 作成日時      |
| Edit Data   | TIMESTAMP | NOT NULL  | 編集日時      |

### Tag
|カラム名   | 型      | 制約     | 説明       |
| -------- | ------- | -------- | --------- |
| ID       | INT     | PK       | タグのID   |
| Name     | VARCHAR | NOT NULL | タグの名前 |

### ArticleTag
|カラム名     | 型  |　制約  |　説明　     |
| ---------- | --- | ------ | ---------- |
| Article ID | INT | PK, FK | Article.ID |
| Tag ID     | INT | PK, FK | Tag.ID     |

## 説明
Article と Tag は多対多関係である。
しかし、SQLでは、1カラムの中にデータは１つずつしか入れないという前提があるので、
ArticleTag を中間テーブルとして採用することで、この問題を解消しました。