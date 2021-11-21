

import random

import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError

from . import *
from beastx.events import register


@register(pattern=".joke$")
async def _(ult):
    await eor(ult, get_joke())


@register(pattern=".insult$")
async def gtruth(ult):
    m = await eor(ult, "Generating...")
    nl = "https://fungenerators.com/random/insult/new-age-insult/"
    ct = requests.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"{cm}")


@register(pattern=".url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await eor(event, "Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(
            event,
            "**Shortened url**==> {}\n**Given url**==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await eor(event, "`Something went wrong. Please try again Later.`")


@register(pattern=".decide$")
async def _(event):
    hm = await eor(event, "`Deciding`")
    r = requests.get("https://yesno.wtf/api").json()
    try:
        await event.reply(r["answer"], file=r["image"])
        await hm.delete()
    except ChatSendMediaForbiddenError:
        await eor(event, r["answer"])


@register(pattern=".xo$")
async def xo(ult):
    xox = await ult.client.inline_query("xobot", "play")
    await xox[random.randrange(0, len(xox) - 1)].click(
        ult.chat_id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()


@register(pattern=".wordi$")
async def word(ult):
    game = await ult.client.inline_query("wordibot", "play")
    await game[0].click(
        ult.chat_id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()


@register(pattern=".gps (.*)")
async def map(ult):
    get = ult.pattern_match.group(1)
    if not get:
        return await eor(ult, "Use this command as `.gps <query>`")
    gps = await ult.client.inline_query("openmap_bot", f"{get}")
    await gps[0].click(
        ult.chat_id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()
   
   
CMD_HELP.update(
    {
        "fun": """**✘ Commands Available
**

• `.joke`
    To get joke.

• `.insult`
    Insult someone..

• `.url <long url>`
    To get a shorten link of long link.

• `.decide`
    Decide something.

• `.xo`
    Opens tic tac game only where using inline mode is allowed.

• `.wordi`
    Opens word game only where using inline mode is allowed.

• `.gps <name of place>`
    Shows the desired place in the map.

"""
    }
)
