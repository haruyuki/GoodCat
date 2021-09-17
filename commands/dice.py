import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_int_slash_option("number", "The number of dice to roll (max: 25).")
@tanjun.as_slash_command("roll", "Roll one or more dice.")
async def command_dice(ctx: tanjun.abc.Context, number: int) -> None:
    if number > 100:
        await ctx.respond("No more than 100 dice can be rolled at once.")
        return

    rolls = [random.randint(1) for i in range(number)]

    await ctx.respond(
        " + ".join(f"{r}" for r in rolls)
        + f" = **{sum(rolls):,}**"
    )


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
