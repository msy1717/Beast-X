"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from beastx import CMD_HELP
from beastx.utils import beastx_cmd, sudo_cmd

from . import *
@beast.on(beastx_cmd("leave"))
@beast.on(sudo_cmd("leave", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        time.sleep(3)
        if e.is_group:
            await e.edit("`I’m not wanted here so I’m leaving.`")
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`Boss, This is Not A Chat`")


CMD_HELP.update(
    {
        "Leave": "**leave**\
\n\n**Syntax : **`.leave`\
\n**Usage :** use this plugin to leave a group."
    }
)
