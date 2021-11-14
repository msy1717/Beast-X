"""
Available Commands:
.HI"""
from beastx import bot as javes
from telethon import events

import asyncio

from beastx.utils import admin_cmd

@javes.on(admin_cmd("hibye"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0,36)
    await event.edit("!hey")
    animation_chars = [
            "OK",
            "HELLO",
            "HI",
            "KOI HAI",
            "ETNA SANNATA Q HAI BHAI",
            "🥺🥺🥺",
            "ETNA CHUP Q HO",
            "🤨🤨🤨🤨🤨",
            "🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻",
            "🤔🤔🤔🤔🤔",
            "👋👋👋",
            "chalo me bhi chala"
            "BYE BYE",
            "🥺🥺🥺🥺🥺",
            "👋",
            "Love You From Heart ❤",
            
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
