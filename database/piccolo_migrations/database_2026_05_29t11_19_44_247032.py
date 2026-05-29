from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import UUID
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod

ID = "2026-05-29T11:19:44:247032"
VERSION = "1.33.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="database", description=DESCRIPTION
    )

    manager.drop_column(
        table_class_name="FriendRequest",
        tablename="friend_request",
        column_name="name",
        db_column_name="name",
        schema=None,
    )

    manager.drop_column(
        table_class_name="FriendRequest",
        tablename="friend_request",
        column_name="popularity",
        db_column_name="popularity",
        schema=None,
    )

    manager.add_column(
        table_class_name="FriendConnection",
        tablename="friend_connection",
        column_name="a_local_ref_for_b",
        db_column_name="a_local_ref_for_b",
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
        table_class_name="FriendConnection",
        tablename="friend_connection",
        column_name="b_local_ref_for_a",
        db_column_name="b_local_ref_for_a",
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
        table_class_name="FriendRequest",
        tablename="friend_request",
        column_name="requestee",
        db_column_name="requestee",
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
        table_class_name="FriendRequest",
        tablename="friend_request",
        column_name="requestor",
        db_column_name="requestor",
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
        table_class_name="FriendRequest",
        tablename="friend_request",
        column_name="requestor_local_ref_for_requestee",
        db_column_name="requestor_local_ref_for_requestee",
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

    manager.rename_column(
        table_class_name="FriendConnection",
        tablename="friend_connection",
        old_column_name="friend1",
        new_column_name="friend_a",
        old_db_column_name="friend1",
        new_db_column_name="friend_a",
        schema=None,
    )

    manager.rename_column(
        table_class_name="FriendConnection",
        tablename="friend_connection",
        old_column_name="friend2",
        new_column_name="friend_b",
        old_db_column_name="friend2",
        new_db_column_name="friend_b",
        schema=None,
    )

    return manager
