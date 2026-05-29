from dataclasses import dataclass

from litestar.contrib.piccolo import PiccoloDTO
from litestar.dto import DTOConfig


@dataclass
class FriendRequestBody:
    friend_request_token: str
    local_reference_uuid: str