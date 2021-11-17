from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.phone import CreateGroupCallRequest
from telethon.tl.functions.phone import DiscardGroupCallRequest
from telethon.tl.functions.phone import GetGroupCallRequest
from telethon.tl.functions.phone import InviteToGroupCallRequest

from . import *

async def getvc(event):
    chat_ = await event.client(GetFullChannelRequest(event.chat_id))
    _chat = await event.client(GetGroupCallRequest(chat_.full_chat.call))
    return _chat.call

def all_users(a, b):
    for c in range(0, len(a), b):
        yield a[c : c + b]


@beast.on(beastx_cmd(pattern="startvc$"))
@beast.on(sudo_cmd(pattern="startvc$", allow_sudo=True))
async def _(event):
    try:
        await event.client(CreateGroupCallRequest(event.chat_id))
        await event.reply("**🔊 Voice Chat Started Successfully**")
    except Exception as e:
        await eor(event, f"`{str(e)}`")


@beast.on(beastx_cmd(pattern="endvc$"))
@beast.on(sudo_cmd(pattern="endvc$", allow_sudo=True))
async def _(event):
    try:
        await beast(DiscardGroupCallRequest(await getvc(event)))
        await event.reply("**📍 Voice Chat Ended Successfully !!**")
    except Exception as e:
        await eor(event, f"`{str(e)}`")


@beast.on(beastx_cmd(pattern="vcinvite$"))
@beast.on(sudo_cmd(pattern="vcinvite$", allow_sudo=True))
async def _(event):
    hell = await event.reply("`🧐 Inviting Users To Voice Chat....`")
    users = []
    i = 0
    async for j in event.client.iter_participants(event.chat_id):
        if not j.beast:
            users.append(j.id)
    hel_ = list(all_users(users, 6))
    for k in hel_:
        try:
            await beast(InviteToGroupCallRequest(call=await getvc(event), users=k))
            i += 6
        except BaseException:
            pass
    await hell.edit(f"**🚀 Invited {i} Users to Voice Chat**")


CMD_HELP.update(
    {
        "Vc Tool": "**VC tool**\
\n\n**Syntax : **`.startvc`\
\n**Usage :** start voice chat in group.\
\n\n**Syntax : **`.endvc`\
\n**Usage :** close vc in group.\n"
    }
)
