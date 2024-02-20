import asyncio


class IsobarInterface:
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        event_manager.subscribe(self)

    async def run(self):
        while True:
            """
            Isobar implementation
            """
            await asyncio.sleep(1)

    def update(self, data):
        print(f"Isobar received: {data}")
