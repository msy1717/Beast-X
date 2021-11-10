from telethon import events
from beastx.util import admin_cmd
from beastx import beast as borg

@borg.on(admin_cmd(pattern="copy"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        reply_to_id = event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(the_real_message)
    else:
        await event.edit("Reply to a message with `.copy` to copy it works on emojis and text")
        
CMD_HELP.update(
    {
        "copy": """✘ Commands Available -

`.copy` as reply to a message to copy

"""
    }
)

        
        
