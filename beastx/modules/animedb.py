#ported from ultroid to Beastx

"""
Search animes and manga from anilist.co using @animedb_bot

✘ Commands Available
• `{i}manga <keyword>`
    To get manga info
"""

from telethon.errors import ChatSendInlineForbiddenError
import requests as r
from bs4 import BeautifulSoup as bs


from . import *

INLOCK = "`Seems like inline messages aren't allowed here`"
eor = edit_or_reply
eod = edit_or_reply
@beast_cmd(
    pattern=".manga ?(.*)",
)
async def manga(ult):
    msg = await eor(ult, "`Searching ...`")
    keyword = ult.pattern_match.group(1)
    if keyword is None:
        return await msg.edit("`Provide a Keyword to search`")
    try:
        animes = await ult.client.inline_query("animedb_bot", f"<m> {keyword}")
        await animes[0].click(
            ult.chat_id,
            reply_to=ult.reply_to_msg_id,
            silent=True if ult.is_reply else False,
            hide_via=True,
        )
        return await msg.delete()
    except Exception:
        return await msg.edit("`No Results Found ...`")

@beast_cmd(pattern=".apod$")
async def aposj(e):
    link = "https://apod.nasa.gov/apod/"
    C = r.get(link).content
    m = bs(C, "html.parser", from_encoding="utf-8")
    try:
        try:
            img = m.find_all("img")[0]["src"]
            img = link + img
        except IndexError:
            img = None
        expla = m.find_all("p")[2].text.replace("\n", " ")
        expla = expla.split("     ")[0]
        if len(expla) > 3000:
            expla = expla[:3000] + "..."
        expla = "__" + expla + "__"
        await e.reply(expla, file=img)
        if e.out:
            await e.delete()
    except Exception as E:
        return await eor(e, str(E))
    
@ultroid_cmd(pattern=".asupan ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await eor(event, "`Something went wrong LOL...`")


@ultroid_cmd(pattern=".wibu ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await eor(event, "`Something went wrong LOL...`")


@ultroid_cmd(pattern=".chika ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await eor(event, "`Something went wrong LOL...`")   

CMD_HELP.update(
    {
        "Addons1": """**Commands in aniquote are **
• `.asupan`
   To send random intake video.
• `.wibu`
   To send a random wibu video.
• `.chika`
   To send a random chikakiku video.
     To send random intake video.
• `.manga`
   To send a random wibu video.
• `.apod`
   To send a random chikakiku video.
 
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
