
from telethon import events
from userbot import bot as javes
import asyncio

from userbot.utils import admin_cmd

@javes.on(admin_cmd("evil"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    await event.edit("☠️EVIL IS WAKE UP...HA...HA...HA ...👽‼️👾")
    animation_chars = [
            "😈",
            "👿",
            "🎃",
            "💀",
            "👻",
            ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
