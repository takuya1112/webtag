from urllib.parse import quote_plus

from decouple import config


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

    DB_USER = config("DB_USER")
    DB_PASSWORD = quote_plus(config("DB_PASSWORD"))
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")
    DB_NAME = config("DB_NAME")

    JWT_SECRET = config("JWT_SECRET")
    JWT_ALGORITHM = config("JWT_ALGORITHM")
    TOKEN_HASH_SECRET = config("TOKEN_HASH_SECRET")

    ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
    REFRESH_TOKEN_EXPIRE_DAYS = config("REFRESH_TOKEN_EXPIRE_DAYS", cast=int)
    REVOKED_REFRESH_TOKEN_EXPIRE_DAYS = config(
        "REVOKED_REFRESH_TOKEN_EXPIRE_DAYS", cast=int
    )

    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
