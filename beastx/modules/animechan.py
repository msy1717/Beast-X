# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/UltroidAddons/>

"""
Fetch Random anime quotes

Command : `{i}aniquote`
"""

import requests

from . import *


@beast_cmd(pattern=".aniquote")
async def _(ult):
    u = await eor(ult, "...")
    try:
        resp = requests.get("https://animechan.vercel.app/api/random").json()
        results = f"**{resp['quote']}**\n"
        results += f" — __{resp['character']} ({resp['anime']})__"
        return await u.edit(results)
    except Exception:
        await u.edit("`Something went wrong LOL ...`")

        
 
CMD_HELP.update(
    {
        "aniquote": """**Commands in aniquote are **
  •  `.aniquote`
 
  
**Function : **__Different kinds of aniquote"""
    }
)