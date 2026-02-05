import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Settings:
    """
    .env ファイルから読み込んだ環境変数に従って
    SQLAlchemy 用の PostgresSQL 接続URLを作成する

    Note:
        @property を使用することでsettings.database_urlのように
        メソッドを属性のように扱えるため可読性の向上を図った

    Example:
        settings = Settings()
        settings.database_url
    """
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD'))
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()