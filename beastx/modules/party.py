 
from beastx import bot as javes
from telethon import events

import asyncio

from beastx.utils import admin_cmd

@javes.on(admin_cmd("party"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    await event.edit("It's Party Time")
    animation_chars = [
            "🍭🍦🍧🍩🍪🎂🍰🧁🍫🍬",
            "🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭",
            "🍧🍩🍪🎂🍰🧁🍫🍬🍭🍦",
            "🍩🍪🎂🍰🧁🍫🍬🍭🍦🍧",
            "🍪🎂🍰🧁🍫🍬🍭🍦🍧🍩",
            "🎂🍰🧁🍫🍬🍭🍦🍧🍩🍪",
            "🍰🧁🍫🍬🍭🍦🍧🍩🍪🎂",
            "🧁🍫🍬🍭🍦🍧🍩🍪🎂🍰",
            "🍫🍬🍭🍦🍧🍩🍪🎂🍰🧁",
            "🍬🍭🍦🍧🍩🍪🎂🍰🧁🍫",
            ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
