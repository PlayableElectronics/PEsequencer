import asyncio


class HardwareInterface:
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager

    async def run(self):
        while True:
            """
            Hardware implementation
            """
            data = input("Hardware updating: ")
            self.event_manager.notify(data)
            await asyncio.sleep(1)
