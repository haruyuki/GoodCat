from importlib import import_module
from pathlib import Path
import logging
import os
import uvloop

from dotenv import load_dotenv

import hikari
import tanjun

GUILD_ID = 358248587026497537

load_dotenv()

bot = hikari.GatewayBot(token=os.getenv("DISCORD", None), logs="DEBUG", intents=hikari.Intents.ALL)
# bot.remove_command("help")

client = tanjun.Client.from_gateway_bot(bot, set_global_commands=GUILD_ID)
client.load_modules(*Path('./commands').glob('*.py'))
client.add_prefix('?')

bot.run()