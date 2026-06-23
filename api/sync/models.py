from dataclasses import dataclass

from litestar.contrib.piccolo import PiccoloDTO


@dataclass
class SyncRequestBody:
    eventType: str
    referenceId: str
    isDelete: bool
    payload: dict