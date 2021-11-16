"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon.utils import pack_bot_file_id

from . import *

@beast.on(beastx_cmd("id"))
@beast.on(sudo_cmd("id", allow_sudo=True))
async def _(event):
    starkisgreat = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await starkisgreat.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                )
            )
        else:
            await starkisgreat.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                )
            )
    else:
        await starkisgreat.edit("Current Chat ID: `{}`".format(str(event.chat_id)))


CMD_HELP.update(
    {
        "get_id": "**Get Id**\
\n\n**Syntax : **`.get_id <reply to media or any message>`\
\n**Usage :** Get ID of any Telegram media, or any user."
    }
)
