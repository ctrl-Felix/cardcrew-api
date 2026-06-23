from dataclasses import dataclass

from litestar.contrib.piccolo import PiccoloDTO
from litestar.dto import DTOConfig


@dataclass
class FriendRequestBody:
    requestorName: str
    friendRequestToken: str
    localReferenceUuid: str

@dataclass
class AcceptFriendRequestBody:
    requestorId: str
    requestorLocaleId: str

@dataclass
class ParsedFriendRequest:
    requestorName: str
    requestorId: str

@dataclass
class ParsedSentFriendRequest:
    localRequesteeId: str

@dataclass
class FriendRequestsResponse:
    incoming_friend_requests: list[ParsedFriendRequest]
    sent_friend_requests: list[ParsedSentFriendRequest]

@dataclass
class FriendResponse:
    localId: str