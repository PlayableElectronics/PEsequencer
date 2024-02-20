from .hardware_interface import HardwareInterface
from .user_interface import UserInterface
from .isobar_interface import IsobarInterface
import asyncio


class Sequencer:
    def __init__(self) -> None:
        self.ui = UserInterface()
        self.hardware = HardwareInterface()
        self.isobar = IsobarInterface()

    def run(self) -> None:
        asyncio.run(self._run_all_tasks())

    async def _run_all_tasks(self) -> None:
        task_ui = asyncio.create_task(self.ui.run())
        task_hardware = asyncio.create_task(self.hardware.run())
        task_isobar = asyncio.create_task(self.isobar.run())
        await asyncio.gather(task_ui, task_hardware, task_isobar)
