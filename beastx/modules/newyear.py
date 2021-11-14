# By @krish1303y Thanks A Lot Bro And A Very New Year To You
# If you steal this without credits You will be the geyest gey ever in the world that you will suck cat's dick.
# Cat beastx owner sandeep chakka hai yaad rakhna 😂

import asyncio
from  beastx import ALIVE_NAME
from beastx.utils import admin_cmd
from beastx import bot as borg
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@borg.on(admin_cmd(pattern="newyear$"))
async def _(event):
    if event.fwd_from:
        return
    lightning_anmation_interval = 4
    ttl = range(0, 29)
    await event.edit("Wishing You a Happy new year to all...")
    chars = [
        f"**Hello!👋**",
        "**Happy New Year To All❤️❤️**",
        f"**{DEFAULTUSER} \nHappy Year Master**",
        "[Happy New Year](https://telegra.ph/file/0682331f14d753862d81e.mp4)",
        "Here's to a bright New Year 😘 and a fond farewell to the old",
        "[Here's to the things that are yet to come, and to the memories that we hold*](https://media.giphy.com/media/8It0HNrGjcTT2/giphy.gif)",
        "May you have a prosperous New Year.🥳",
        "[Dont feel sad this new year is day of happiness!](https://media.giphy.com/media/l2JJurAjg3LRPcYHS/giphy.gif)",
        "Wave goodbye to the old👋👋 and embrace the new with hope, dreams, and ambition.",
        "Wishing you a Happy New Year full of happines",
        "First you take a drink🥴, then the drink takes a drink🤒, then the drink takes you.😂",
        "[Some Gifts](https://media.giphy.com/media/3o6fJcIM6mG3Ad6lAk/giphy.gif)",
        "[Some Gifts](https://telegra.ph/file/085ca270bf29e1f2b4c10.mp4)",
        "Here is also 🎁Gifts🎁 from me👨.",
        "[Some Gifts](https://wallpapercave.com/wp/wp7891467.jpg)",
        "[Some Gifts](https://media.giphy.com/media/3j4QTXSIKRfPCgvVIL/giphy.gif)",
        "[Some Gifts](https://media.giphy.com/media/s2qXK8wAvkHTO/giphy.gif)",
        "[Some Gifts](https://telegra.ph/file/0c3f83a170e28b30316ae.mp4)",
        f"Once Again Happy New Year To All By {DEFAULTUSER}❤️❤️❤️",  
        f"Once Again Happy New Year To All By {DEFAULTUSER}😘😘😘",
        f"Once Again Happy New Year To All By {DEFAULTUSER}❤️❤️❤️", 
        f"Once Again Happy New Year To All By {DEFAULTUSER}💜💜💜",
        f"Once Again Happy New Year To All By {DEFAULTUSER}❤️❤️❤️",  
        f"Once Again Happy New Year To All By {DEFAULTUSER}💛💛💛",     
        f"Once Again Happy New Year To All By {DEFAULTUSER}❤️❤️❤️",  
        f"Once Again Happy New Year To All By {DEFAULTUSER}🧡🧡🧡",      
        f"Once Again Happy New Year To All By {DEFAULTUSER}💙💙💙",
        f"Once Again Happy New Year To All By {DEFAULTUSER}💚💚💚",  
        f"Once Again Happy New Year To All By {DEFAULTUSER}❤️❤️❤️",  
        f"Once Again Happy New Year To All By {DEFAULTUSER}**💖💖💖",
        ]

    for i in ttl:  

        await asyncio.sleep(lightning_anmation_interval)
        await event.edit(
            chars[i % 30], link_preview=True
        )
