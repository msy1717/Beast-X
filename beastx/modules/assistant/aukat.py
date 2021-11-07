from .. import xmrunal
from telethon import events, Button

@xmrunal.on(events.NewMessage(incoming=True, pattern="/test143"))
async def start(event):
    await event.reply("Hello!")

