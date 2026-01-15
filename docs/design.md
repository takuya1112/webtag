# WebTag 設計書

## 1.データ設計

### エンティティ一覧
Article
|カラム名      | 型　     　| 
| ----------- | ---------- |
| Article ID  | INT      　| (PK)
| Title       | VARCHAR  　|
| Web Link    | VARCHAR  　| 
| Create Data | TIMESTAMP |
| Edit Data   | TIMESTAMP |

Tag
|カラム名   | 型      |
| -------- | ------- |
| Tag ID   | INT     | (PK)
| Tag Name | VARCHAR |

ArticleTag
|カラム名     | 型  |
| ---------- | --- |
| Article ID | INT | (PK FK)
| Tag ID     | INT | (PK FK)

## 設計上の判断
Article と Tag は多対多関係である。
しかし、SQLでは、1カラムの中にデータは１つずつしか入れないという前提があるので、
ArticleTag を中間テーブルとして採用しました。