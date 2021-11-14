
import random
from beastx import CMD_HELP
from beastx.events import register
from beastx.utils import admin_cmd
from telethon import events, types, functions, utils

from beastx import bot as borg

import asyncio
def choser(cmd, pack, blacklist={}):
    docs = None

    @borg.on(events.NewMessage(pattern=rf'\.{cmd}', outgoing=True))
    async def handler(event):

        if event.fwd_from:
            return
        animation_interval = 3
        animation_ttl = range(0,5)
        nonlocal docs
        
        for i in animation_ttl:
                    
               await asyncio.sleep(animation_interval)
               if docs is None:
                    docs = [
                        utils.get_input_document(x)
                        for x in (await borg(functions.messages.GetStickerSetRequest(types.InputStickerSetShortName(pack)))).documents
                    ]

               await event.respond(file=random.choice(docs))

choser('hpdiwali', 'a929138153_by_Shivam_Patel_1_anim')
