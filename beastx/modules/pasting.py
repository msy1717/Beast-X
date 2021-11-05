



# Made by @e3ris for Ultroid
# < https://github.com/TeamUltroid/Ultroid >

# Thanks to [Avish and MoonLight] for making DogBin clones :^)

"""
✘ **Alternative Paste and Logs Plugin >.<**

✘ **CMDs available:**
>>  `{i}ilogs`
>>  `{i}ipaste (some_text)`

•• You can use [-d, -s] flags with ipaste.
"""

import requests
import json
import os

from uniborg.util import edit_or_reply, beastx_cmd, sudo_cmd,admin_cmd

from beastx import CMD_HELP
from beastx import beast
from beastx.utils import register as beast_cmd


c1 = "https://dogebin.up.railway.app/" # Moonlight
c2 = "https://dogbin.up.railway.app/" # Avish

spaceb_url = "https://spaceb.in/api/v1/documents/"

def spacebin(data, ext="txt"):
    try:
        request = requests.post(
            spaceb_url, 
            data={
                "content": data.encode("UTF-8"),
                "extension": ext,
            },
        )
    except Exception as ex:
        return f"#Error : {ex}"
    r = request.json()
    key = r.get('payload').get('id')
    if key is not None:
        return {
            "bin": "SpaceBin",
            "link": f"https://spaceb.in/{key}",
            "raw": f"{spaceb_url}{key}/raw",
        }
    else:
        return "#Error : No response."


def dogbin(data, site=c2, ext="txt"):
    dog_bin = c1 if site == "c1" else c2
    try:
        request = requests.post(
            url=f'{dog_bin}documents',
            data=json.dumps({"content": data}),
            headers = {"content-type": "application/json"},
        )
    except Exception as ex:
        return f"#Error : {ex}"
    r = request.json()
    key = r.get("key")
    if key is not None:
        link = (
            f"{dog_bin}v/{key}" if r.get("isUrl") else f"{dog_bin}{key}")
        return {
            "bin": "DogBin",
            "link": f"{link}.{ext}",
            "raw": f"{dog_bin}raw/{key}",
        }
    else:
        return "#Error : Bad Response."


def rpaste(data, ext="txt"):
    pasta_ = dogbin(data, 'c2', ext)
    if isinstance(pasta_, dict):
        return pasta_
    else:
        pasta_ = spacebin(data, ext)
        if isinstance(pasta_, dict):
            return pasta_
        else:
            pasta_ = dogbin(data, 'c1', ext)
            if isinstance(pasta_, dict):
                return pasta_
            else:
                return "#Error : Couldn't paste on any pastebin."


@beast_cmd(pattern="ipaste ?(-d|-s|) ?(.*)")
async def ipaste(e):
    if e.fwd_from:
        return
    data, ext = '', 'txt'
    pastebin = e.pattern_match.group(1)
    args = e.pattern_match.group(2)
    eris = await edit_or_reply(e, "`pasting..`")
    if e.is_reply:
        reply = await e.get_reply_message()
        if reply.media:
            if reply.file.size > 15000000: # 14MB
                return await edit_or_reply(eris, "`File too big to paste`")
            try:
                ext = reply.file.ext.replace('.', '')
                _dl = await e.client.download_media(reply)
                with open(_dl, 'r') as f:
                    data = f.read()
                    f.close()
            except Exception as ex:
                return await eris.edit(f'#Error : `{ex}`')
            finally:
                os.remove(_dl)
        else:
            data = reply.message
    elif args:
        data = args
    else:
        await edit_or_reply(eris, "`Reply to a msg/file..`")
        return

    # pastebins -_-
    if pastebin == "-d":
        out = dogbin(data, 'c2', ext)
    elif pastebin == "-s":
        out = spacebin(data, ext)
    else:
        out = rpaste(data, ext)

    if isinstance(out, dict):
        c1m = f"<b>Pasted to <a href='{out['link']}'>{out['bin']}</a> "\
        f"| <a href='{out['raw']}'>Raw</a></b>"
        await eris.edit(c1m, parse_mode="html", link_preview=False)
    else:
        return await edit_or_reply(eris, str(out))

      
CMD_HELP.update(
    {
        "Paste": ".paste <reply to a file>\nUse - Read contents of file and send telegram message to spacebin to read doc."
    }
)


