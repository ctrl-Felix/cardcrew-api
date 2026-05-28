import datetime
import uuid

from piccolo.columns import Integer, Varchar
from piccolo.columns.column_types import Timestamptz, UUID
from piccolo.table import Table

from piccolo_conf import DB


class User(Table, tablename="users", db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    device_token = Varchar(length=256)
    friend_request_token = Varchar(length=8)


class RefreshToken(Table, tablename="refresh_tokens", db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    user_id = UUID()
    token_hash = Varchar(length=64)  # SHA-256 hex of the raw token
    expires_at = Timestamptz(default=datetime.datetime.now)


class FriendRequest(Table, db=DB):
    name = Varchar(length=100)
    popularity = Integer()

class FriendConnection(Table, db=DB):
    friend1 = UUID()
    friend2 = UUID()

class Match(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    title = Varchar(length=100)

class MatchParticipants(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    user_id = UUID()

class MatchRound(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    user_id = UUID()
    score = Integer()
