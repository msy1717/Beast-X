
import requests as r
from telegraph import upload_file as uf

from . import *

TE = f"API not found, Please get it from ocr.space and set\n\ncommand `{HNDLR}setredis OCR_API your-api-key`"


@beast_cmd(pattern=".ocr ?(.*)")
async def ocrify(ult):
    if not ult.is_reply:
        return await eor(ult, "`Reply to Photo...`")
    msg = await eor(ult, "`Processing..`")
    OAPI = udB.get("OCR_API")
    if not OAPI:
        return await msg.edit(TE)
    pat = ult.pattern_match.group(1)
    repm = await ult.get_reply_message()
    if not (repm.media and repm.media.photo):
        return await msg.edit("`Not a Photo..`")
    dl = await repm.download_media()
    if pat:
        atr = f"&language={pat}&"
    else:
        atr = "&"
    tt = uf(dl)
    li = "https://telegra.ph" + tt[0]
    gr = r.get(
        f"https://api.ocr.space/parse/imageurl?apikey={OAPI}{atr}url={li}"
    ).json()
    trt = gr["ParsedResults"][0]["ParsedText"]
    await msg.edit(f"**🎉 OCR PORTAL\n\nRESULTS ~ ** `{trt}`")
CMD_HELP.update(
    {
        "ocr": """✘ Commands Available -

• `.ocr <language code><reply to a photo>`
    text recognition service.


"""
    }
)
