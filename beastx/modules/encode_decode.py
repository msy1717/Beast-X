



import base64

from . import *


@beast_cmd(pattern=".encode ?(.*)")
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await eor(e, "`Give me Something to Encode..`")
    byt = match.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await eor(e, f"**=>> Encoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`")


@beast_cmd(pattern=".decode ?(.*)")
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await eor(e, "`Give me Something to Decode..`")
    byt = match.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await eor(e, f"**=>> Decoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`")
    except Exception as p:
        await eor(e, "**ERROR :** " + str(p))

CMD_HELP.update(
    {
        "encode/decode": """**✘ Commands Available
**

• {i}encode <text/reply to message>
    encode the text

 • {i}decode <text/reply to message>
    decode the text

"""
    }
)