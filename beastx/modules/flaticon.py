
import os
import random

import requests
from bs4 import BeautifulSoup as bs

from . import *


@beast_cmd(pattern=".icon ?(.*)")
async def www(e):
    a = e.pattern_match.group(1)
    if not a:
        return await eor(e, "Give some Text to Get Icon from Flaticon.com")
    tt = await eor(e, "`Processing...`")
    query = a.replace(" ", "%20")
    try:
        link = f"https://www.flaticon.com/search?word={query}"
        ge = requests.get(link).content
        cl = bs(ge, "lxml", from_encoding="utf-8")
        results = cl.find_all(
            "img", src="https://media.flaticon.com/dist/min/img/loader.gif"
        )
        dome = results[random.randrange(0, len(results) - 1)]["data-src"]
        await download_file(dome, "sticker.webp")
        await e.reply(file="sticker.webp")
        os.remove("sticker.webp")
        await tt.delete()
    except Exception as E:
        LOGS.info(E)
        await tt.edit("`No Results Found`")

        

        
CMD_HELP.update(
    {
        "Flaticon": """**✘ Commands Available
**
• `.icon <query>`
    Icon search from flaticon.com and uploading as sticker.

"""
    }
)