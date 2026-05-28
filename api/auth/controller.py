import datetime
import hashlib
import random
import secrets
import string
import uuid

import bcrypt
import jwt
from litestar import Controller, post
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT

from api.auth.models import LoginRequest, LogoutRequest, RefreshRequest, RegisterRequest, TokenResponse, \
    AnonRegisterRequest, AnonRegisterResponse
from config import AppConfig
from database.tables import RefreshToken, User as UserTable


class AuthController(Controller):
    path = "/auth"
    tags = ["Auth"]

    @post("/anonymous-register", exclude_from_auth=True)
    async def registerUserAnonymously(self, data: AnonRegisterRequest) -> AnonRegisterResponse:
        device_token = str(uuid.uuid4())
        friend_request_token = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))

        user = UserTable(id=data.id, device_token=device_token, friend_request_token=friend_request_token)

        await user.save().run()

        return AnonRegisterResponse(
            friend_request_token=friend_request_token,
            device_token=device_token
        )




def _hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def _create_access_token(user_id: str) -> str:
    expiry = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=AppConfig.ACCESS_TOKEN_DURATION_MINUTES
    )
    return jwt.encode({"sub": user_id, "exp": expiry}, AppConfig.JWT_SECRET, algorithm="HS256")


async def _create_token_pair(user_id: uuid.UUID) -> TokenResponse:
    raw_refresh = secrets.token_urlsafe(32)

    stored = RefreshToken(
        user_id=user_id,
        token_hash=_hash_token(raw_refresh),
        expires_at=datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(days=AppConfig.REFRESH_TOKEN_DURATION_DAYS),
    )
    await stored.save().run()

    return TokenResponse(
        access_token=_create_access_token(str(user_id)),
        refresh_token=raw_refresh,
    )
