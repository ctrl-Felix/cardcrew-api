from litestar import Controller, get


class MatchController(Controller):
    path = "/match"
    tags = ["Match"]

    @get("/plz")
    async def placeholderCall(self) -> None:
        return