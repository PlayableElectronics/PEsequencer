import asyncio


class IsobarInterface:
    def __init__(self) -> None:
        pass

    async def run(self):
        while True:
            """
            Isobar implementation
            """
            await asyncio.sleep(1)
