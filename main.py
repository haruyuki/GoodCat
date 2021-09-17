from importlib import import_module
from pathlib import Path
import logging
import os
import uvloop

import hikari
import tanjun

GUILD_ID = 358248587026497537

bot = hikari.GatewayBot(token='NDYzOTAxMDQ0MDg3NDU1NzY3.Wzw3gw.DxK0sSfW_k4ziMb1iB-Bz4x1kvY', logs="DEBUG", intents=hikari.Intents.ALL)
# bot.remove_command("help")

client = tanjun.Client.from_gateway_bot(bot, set_global_commands=GUILD_ID)
client.load_modules(*Path('./commands').glob('*.py'))
client.add_prefix('?')

bot.run()