import asyncio
from datetime import datetime

from . import *
firethumb = "./resources/beastxthumb.jpg"


@beast.on(beastx_cmd(pattern="send ?(.*)"))
@beast.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    the_plugin_file = "./beastx/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"Plugin Name - {input_str}.py \nUploaded By Beast-X"
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=firethumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "send": "**Send**\
\n\n**Syntax : **`.send <plugin name>`\
\n**Usage :** sends the plugin."
    }
)
