import datetime

from litestar import Controller, post, Request
from litestar.exceptions import NotFoundException

from api.sync.models import SyncRequestBody
from database.tables import Match, LocalPlayer, User, MatchParticipants, MatchRound


class SyncController(Controller):
    path = "/sync"
    tags = ["Sync"]

    @post("/upload")
    async def upload_event(self, data: SyncRequestBody, request: Request) -> None:

        if data.eventType == "match":
            match = await Match().objects().get(Match.id == data.referenceId)
            payload = data.payload
            timestamp = datetime.datetime.fromtimestamp(data.payload.pop("createdAt") / 1000, tz=datetime.timezone.utc)

            if not match:
                await Match().insert(Match(**payload, createdAt=timestamp))
            else:
                for key, value in payload.items():
                    setattr(match, key, value)
                match.lastUpdated = datetime.datetime.now()
                match.createdAt = timestamp
                await match.save()
            return
        elif data.eventType == "player":
            if data.referenceId == request.user.id:
                return

            lp = await LocalPlayer().objects().get(LocalPlayer.id == data.referenceId)

            if not lp:
                await LocalPlayer().insert(LocalPlayer(**data.payload, belongsToUserId=request.user.id))
            else:
                for key, value in data.payload.items():
                    setattr(lp, key, value)
                lp.lastUpdated = datetime.datetime.now()
                await lp.save()
            return

        elif data.eventType == "match_participant":

            mp = await MatchParticipants().objects().get(MatchParticipants.id == data.referenceId)
            payload = data.payload
            created_at = datetime.datetime.fromtimestamp(data.payload.pop("createdAt") / 1000, tz=datetime.timezone.utc)

            if not mp:
                await MatchParticipants().insert(MatchParticipants(**payload, createdAt=created_at))
            else:
                for key, value in payload.items():
                    setattr(mp, key, value)
                mp.lastUpdated = datetime.datetime.now()
                mp.createdAt = created_at
                await mp.save()
            return
        elif data.eventType == "match_round":

            mr = await MatchRound().objects().get(MatchRound.id == data.referenceId)
            payload = data.payload
            created_at = datetime.datetime.fromtimestamp(data.payload.pop("createdAt") / 1000, tz=datetime.timezone.utc)

            if not mr:

                await MatchRound().insert(MatchRound(**payload, createdAt=created_at))
            else:
                for key, value in payload.items():
                    setattr(mr, key, value)
                mr.lastUpdated = datetime.datetime.now()
                mr.createdAt = created_at
                await mr.save()
            return

        else:
            request.logger.warn(f"The event type {data.eventType} isn't implemented yet")
            raise NotFoundException()

