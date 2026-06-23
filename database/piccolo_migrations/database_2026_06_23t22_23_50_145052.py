from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.column_types import UUID
from piccolo.columns.defaults.timestamptz import TimestamptzNow
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod

ID = "2026-06-23T22:23:50:145052"
VERSION = "1.33.0"
DESCRIPTION = "adapt match round and participants to schema"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="database", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="MatchParticipants",
        tablename="match_participants",
        column_name="createdAt",
        db_column_name="createdAt",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
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

    manager.add_column(
        table_class_name="MatchParticipants",
        tablename="match_participants",
        column_name="lastUpdated",
        db_column_name="lastUpdated",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
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

    manager.add_column(
        table_class_name="MatchParticipants",
        tablename="match_participants",
        column_name="matchId",
        db_column_name="matchId",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
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

    manager.add_column(
        table_class_name="MatchRound",
        tablename="match_round",
        column_name="createdAt",
        db_column_name="createdAt",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
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

    manager.add_column(
        table_class_name="MatchRound",
        tablename="match_round",
        column_name="lastUpdated",
        db_column_name="lastUpdated",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
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

    manager.add_column(
        table_class_name="MatchRound",
        tablename="match_round",
        column_name="matchId",
        db_column_name="matchId",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
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

    manager.add_column(
        table_class_name="MatchRound",
        tablename="match_round",
        column_name="roundId",
        db_column_name="roundId",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
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

    manager.rename_column(
        table_class_name="MatchParticipants",
        tablename="match_participants",
        old_column_name="user_id",
        new_column_name="playerId",
        old_db_column_name="user_id",
        new_db_column_name="playerId",
        schema=None,
    )

    manager.rename_column(
        table_class_name="MatchRound",
        tablename="match_round",
        old_column_name="user_id",
        new_column_name="playerId",
        old_db_column_name="user_id",
        new_db_column_name="playerId",
        schema=None,
    )

    return manager
