from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Boolean
from piccolo.columns.indexes import IndexMethod

ID = "2026-06-23T22:27:43:172931"
VERSION = "1.33.0"
DESCRIPTION = "adapt match round and participants to schema"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="database", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="MatchParticipants",
        tablename="match_participants",
        column_name="isHidden",
        db_column_name="isHidden",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
