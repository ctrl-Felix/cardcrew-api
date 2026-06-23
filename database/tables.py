import datetime
import uuid

from piccolo.columns import Integer, Varchar, Boolean
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
    requestor = UUID()
    requestor_name = Varchar(length=255)
    requestor_local_ref_for_requestee = UUID()
    requestee = UUID()

class FriendConnection(Table, db=DB):
    friend_a = UUID()
    a_local_ref_for_b = UUID()
    friend_b = UUID()
    b_local_ref_for_a = UUID()

# These tables are replicates from the local databases and therefore camelcase
class Match(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    title = Varchar(length=100)
    description = Varchar(length=255)
    status = Varchar(length=32)
    createdAt = Timestamptz()
    lastUpdated=Timestamptz(default=datetime.datetime.now)

class LocalPlayer(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    belongsToUserId = UUID()
    name = Varchar(length=100)
    lastUpdated=Timestamptz(default=datetime.datetime.now)

class MatchParticipants(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    matchId = UUID()
    playerId = UUID()
    createdAt = Timestamptz()
    isHidden = Boolean()
    lastUpdated=Timestamptz(default=datetime.datetime.now)

class MatchRound(Table, db=DB):
    id = UUID(primary_key=True, default=uuid.uuid4)
    matchId = UUID()
    playerId = UUID()
    roundId = Integer()
    score = Integer()
    createdAt = Timestamptz()
    lastUpdated=Timestamptz(default=datetime.datetime.now)

