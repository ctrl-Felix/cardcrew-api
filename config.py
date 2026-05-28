import os


class AppConfig:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_DATABASE = os.getenv("DB_DATABASE", "psql")
    DB_USERNAME = os.getenv("DB_USERNAME", "psql")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "psql")

    JWT_SECRET = os.getenv("JWT_SECRET", "change-me-in-production")
    ACCESS_TOKEN_DURATION_MINUTES = int(os.getenv("ACCESS_TOKEN_DURATION_MINUTES", "15"))
    REFRESH_TOKEN_DURATION_DAYS = int(os.getenv("REFRESH_TOKEN_DURATION_DAYS", "30"))