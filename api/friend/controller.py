from litestar import Controller, post, get, Request
from litestar.exceptions import NotFoundException

from api.friend.models import FriendRequestBody, ParsedFriendRequest, FriendRequestsResponse, ParsedSentFriendRequest, \
    AcceptFriendRequestBody, FriendResponse
from database.tables import User, FriendRequest, FriendConnection
from piccolo_conf import DB


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
        requestee = await User.objects().get(User.friend_request_token == data.friendRequestToken).run()
        if not requestee:
            raise NotFoundException()

        await FriendRequest.insert(FriendRequest(
            requestor_name=data.requestorName,
            requestor=request.user.id,
            requestor_local_ref_for_requestee=data.localReferenceUuid,
            requestee=requestee.id
        ))

        return

    @post("/accept-friend-request")
    async def accept_friend_request(self, data: AcceptFriendRequestBody, request: Request) -> None:
        friend_request = await FriendRequest.objects().get(
            (FriendRequest.requestor == data.requestorId)
            & (FriendRequest.requestee == str(request.user.id))
        )
        if friend_request is None:
            raise NotFoundException(detail="Friend Request not found")

        new_friend_connection = FriendConnection(
            friend_a=friend_request.requestor,
            a_local_ref_for_b = friend_request.requestor_local_ref_for_requestee,
            friend_b =friend_request.requestee,
            b_local_ref_for_a = data.requestorLocaleId

        )

        async with DB.transaction():
            await FriendConnection.insert(new_friend_connection)
            await friend_request.remove()
        return

    @get("/list")
    async def list_all_friends(self, request: Request) -> list[FriendResponse]:
        connections = await (FriendConnection().objects().where((FriendConnection.friend_a == request.user.id) | (FriendConnection.friend_b == request.user.id)))

        retdata = []
        for con in connections:
            if con.friend_b == request.user.id:
                retdata.append(FriendResponse(localId=con.b_local_ref_for_a))
            else:
                retdata.append(FriendResponse(localId=con.a_local_ref_for_b))

        return retdata

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