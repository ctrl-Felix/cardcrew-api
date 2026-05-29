from http.client import HTTPException

from litestar import Controller, post, get, Request
from litestar.contrib.piccolo import PiccoloDTO
from litestar.exceptions import NotFoundException
from piccolo.table import Table

from api.friend.models import FriendRequestBody
from database.tables import User, FriendRequest


class FriendController(Controller):
    path = "/friend"

    tags = ["Friend"]

    @get("/pre-check-friend-request")
    async def check_if_friend_request_possible(self, fr_token: str) -> str:
        user = await User.objects().get(User.friend_request_token == fr_token)
        if not user:
            raise NotFoundException(detail="Friend Request Token not found")
        else:
            return "yes"

    @post("/friend-request")
    async def create_friend_request(self, data: FriendRequestBody, request: Request) -> None:

        # Check the frt exists
        requestee = await User.objects().get(User.friend_request_token == data.friend_request_token).run()
        print(data)
        if not requestee:
            raise NotFoundException()

        await FriendRequest.insert(FriendRequest(
            requestor=request.user.id,
            requestor_local_ref_for_requestee=data.local_reference_uuid,
            requestee=requestee.id
        ))

        return
