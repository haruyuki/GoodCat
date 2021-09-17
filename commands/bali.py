import random

import tanjun

component = tanjun.Component()

@component.with_command
@tanjun.as_message_command("bali", "八狸")
async def command_bali(ctx: tanjun.abc.Context) -> None:
	responses = ['八狸可愛', '八狸可幹', '八狸可口']
	await ctx.message.delete()
	await ctx.respond(random.choice(responses))

@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    # This loads the component, and is necessary in EVERY module,
    # otherwise you'll get an error.
    client.add_component(component.copy())