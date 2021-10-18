import asyncio
from pathlib import Path
import logging
import os
import uvloop

from dotenv import load_dotenv

import hikari
import tanjun

from goodcat import GUILD_ID, __version__

from .client import Client

load_dotenv()

logger = logging.getLogger("goodcat.main")

class Bot(hikari.GatewayBot):
    def __init__(self) -> None:
        super().__init__(token=os.environ.get("DISCORD"), logs="DEBUG", intents=hikari.Intents.ALL)

    def create_client(self) -> None:
        self.client = Client.from_gateway_bot(self, set_global_commands=GUILD_ID)
        self.client.load_modules()
        self.client.add_prefix("?")

    def run(self: hikari.GatewayBot) -> None:
        self.create_client()

        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)

        super().run()

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        await self.client.open()
        logger.info("Bot is starting...")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        await self.update_presence(
            activity=hikari.Activity(type=hikari.ActivityType.PLAYING, name="狗狗")
        )
        logger.info("Bot is loaded!")

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        await self.client.close()
        logger.info("Bot has been shut down.")
# bot.remove_command("help")
