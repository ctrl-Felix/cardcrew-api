import uuid

import jwt
from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.middleware import AbstractAuthenticationMiddleware, AuthenticationResult

from api.auth.models import AuthUser
from config import AppConfig
from database.tables import User as UserTable

API_KEY_HEADER = "Authorization"


class JWTAuthMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(self, connection: ASGIConnection) -> AuthenticationResult:
        auth_header = connection.headers.get(API_KEY_HEADER)
        if not auth_header or not auth_header.startswith("Bearer "):
            raise NotAuthorizedException()

        token = auth_header[len("Bearer "):]

        # Temporary solution
        user = await UserTable.objects().get(UserTable.device_token == token).run()
        if not user:
            raise NotAuthorizedException()
        print(user)
        return AuthenticationResult(user=AuthUser(id=str(user.id)), auth=token)


        try:
            payload = jwt.decode(token, AppConfig.JWT_SECRET, algorithms=["HS256"])
        except jwt.PyJWTError:
            raise NotAuthorizedException()

        user_id = payload.get("sub")
        if not user_id:
            raise NotAuthorizedException()

        try:
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            raise NotAuthorizedException()

        users = await UserTable.objects().get(UserTable.id == user_uuid)
        if not users:
            raise NotAuthorizedException()

        db_user = users
        return AuthenticationResult(user=AuthUser(id=str(db_user.id), email="PLACEHOLDER"), auth=token)
