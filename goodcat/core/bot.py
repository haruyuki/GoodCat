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
        self.component_client = tanjun.Client.from_gateway_bot(self)

    def create_client(self: hikari.GatewayBot) -> None:
        self.client = Client.from_gateway_bot(self, set_global_commands=GUILD_ID)
        self.client.load_modules()
        self.client.add_prefix("?")

    def run(self: hikari.GatewayBot) -> None:
        self.create_client()

        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)

        super().run()

    async def on_starting(self: hikari.GatewayBot, event: hikari.StartingEvent) -> None:
        await self.component_client.open()
        logger.info("Bot is starting...")

    async def on_started(self: hikari.GatewayBot, event: hikari.StartedEvent) -> None:
        await self.update_presence(
            activity=hikari.Activity(type=hikari.ActivityType.PLAYING, name="狗狗")
        )
        logger.info("Bot is loaded!")

    async def on_stopping(self: hikari.GatewayBot, event: hikari.StoppingEvent) -> None:
        await self.component_client.close()
        logger.info("Bot has been shut down.")


bot = hikari.GatewayBot(
    token=os.getenv("DISCORD", None), logs="DEBUG", intents=hikari.Intents.ALL
)
# bot.remove_command("help")
