from typing import Any

from litestar import Litestar, Request, get
from litestar.middleware import DefineMiddleware
from litestar.response import Redirect

from api.auth.controller import AuthController
from api.auth.middleware import JWTAuthMiddleware
from api.auth.models import AuthUser
from api.friend.controller import FriendController
from api.match.controller import MatchController
from api.sync.controller import SyncController
from piccolo_conf import DB


async def open_db_connection() -> None:
    await DB.start_connection_pool()


async def close_db_connection() -> None:
    await DB.close_connection_pool()


@get("/", include_in_schema=False)
async def index() -> Redirect:
    return Redirect(path="/schema/swagger")


@get("/me")
async def me(request: Request[AuthUser, str, Any]) -> AuthUser:
    return request.user


app = Litestar(
    route_handlers=[index, AuthController, me, MatchController, FriendController, SyncController],
    middleware=[
        DefineMiddleware(
            JWTAuthMiddleware,
            exclude=[r"^/schema", r"^/$"],
        )
    ],
    on_startup=[open_db_connection],
    on_shutdown=[close_db_connection],
)
