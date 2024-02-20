import asyncio


class UserInterface:
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        event_manager.subscribe(self)

    async def run(self):
        while True:
            """
            User Interface implementation
            """
            await asyncio.sleep(1)

    def update(self, data):
        print(f"UI updated with: {data}")
