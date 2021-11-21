import asyncio

from telethon.events import NewMessage as NewMsg

from . import *
from beastx.events import register


@register(pattern=".del$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if msg_src:
        try:
            await msg_src.delete()
            await delme.delete()
        except Exception as e:
            await eor(
                delme, f"Couldn't delete the message.\n\n**ERROR:**\n`{e}`", time=5
            )
