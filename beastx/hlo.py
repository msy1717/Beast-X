from . import *

import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from beastx import CMD_HELP, lang

@beast.on(beastx_cmd(pattern="hi ?(.*)"))
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "🌺"
    await edit_or_reply(
        event,
        f"{ult}✨✨{ult}✨{ult}{ult}{ult}\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}{ult}{ult}{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨{ult}{ult}{ult}\n☁️☁️☁️☁️☁️☁️☁️☁️",
    )
    
@beast.on(beastx_cmd(pattern="hello"))
async def hello(bst):
  await bst.edit('''
╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝
 ''')
CMD_HELP.update(
    {
        "Hello/hi": """**Plugin : **`Hello/hi`
        
**Commands in animation2 are **
  •  `.hi`
  •  `.hello`
  
  
**Function : **__sends animated hello/hi.__**"""
    }
