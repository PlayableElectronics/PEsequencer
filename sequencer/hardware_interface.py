import asyncio


class HardwareInterface:
    def __init__(self) -> None:
        pass

    async def run(self):
        while True:
            """
            Hardware implementation
            """
            await asyncio.sleep(1)
