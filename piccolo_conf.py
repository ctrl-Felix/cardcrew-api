from piccolo.engine.postgres import PostgresEngine
from config import AppConfig

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": AppConfig.DB_DATABASE,
        "user": AppConfig.DB_USERNAME,
        "password": AppConfig.DB_PASSWORD,
        "host": AppConfig.DB_HOST,
        "port": 5432,
    }
)


APP_REGISTRY = AppRegistry(
    apps=["database.piccolo_app"]
)