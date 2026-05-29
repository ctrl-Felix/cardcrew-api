from typing import Any

from litestar import Litestar, Request, get
from litestar.middleware import DefineMiddleware

from api.auth.controller import AuthController
from api.auth.middleware import JWTAuthMiddleware
from api.auth.models import AuthUser
from api.friend.controller import FriendController
from api.match.controller import MatchController
from piccolo_conf import DB


async def open_db_connection() -> None:
    await DB.start_connection_pool()


async def close_db_connection() -> None:
    await DB.close_connection_pool()


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/me")
async def me(request: Request[AuthUser, str, Any]) -> AuthUser:
    return request.user


app = Litestar(
    route_handlers=[index, AuthController, me, MatchController, FriendController],
    middleware=[
        DefineMiddleware(
            JWTAuthMiddleware,
            exclude=[r"^/schema", r"^/$"],
        )
    ],
    on_startup=[open_db_connection],
    on_shutdown=[close_db_connection],
)
