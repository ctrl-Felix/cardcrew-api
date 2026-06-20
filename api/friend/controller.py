from http.client import HTTPException

from litestar import Controller, post, get, Request
from litestar.contrib.piccolo import PiccoloDTO
from litestar.exceptions import NotFoundException
from piccolo.table import Table

from api.friend.models import FriendRequestBody, ParsedFriendRequest, FriendRequestsResponse, ParsedSentFriendRequest
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
        if not requestee:
            raise NotFoundException()

        await FriendRequest.insert(FriendRequest(
            requestor_name=data.requestorName,
            requestor=request.user.id,
            requestor_local_ref_for_requestee=data.local_reference_uuid,
            requestee=requestee.id
        ))

        return

    @post("/accept-friend-request")
    async def accept_friend_request(self, data: FriendRequestBody, request: Request) -> None:
        return


    @get("/friend-request")
    async def get_friend_requests(self, request: Request) -> FriendRequestsResponse:
        friend_requests = await FriendRequest.objects().where(FriendRequest.requestee == str(request.user.id)).run()

        parsed_friend_requests = []
        for fr in friend_requests:
            requestor = await User.objects().get(User.id == fr.requestor).run()
            if not requestor:
                continue

            parsed_friend_requests.append(ParsedFriendRequest(
                requestorId=str(fr.requestor),
                requestorName=fr.requestor_name
            ))

        parsed_sent_friend_requests = []
        sent_friend_requests = await FriendRequest.objects().where(FriendRequest.requestor == request.user.id).run()
        for fr in sent_friend_requests:
            parsed_sent_friend_requests.append(ParsedSentFriendRequest(
                localRequesteeId=str(fr.requestor_local_ref_for_requestee),
            ))


        return FriendRequestsResponse(
            incoming_friend_requests=parsed_friend_requests,
            sent_friend_requests=parsed_sent_friend_requests
        )