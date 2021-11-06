from . import *
import asyncio
import datetime
from datetime import datetime
from telethon import events
from telethon.tl import functions, types
from beastx import CMD_HELP, lang


@beast.on(beastx_cmd(pattern="hello"))
async def hello(bst):
  await bst.edit('''
╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝
 ''')


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

@beast.on(beastx_cmd(pattern="okboss"))
async def okboss(ult):
 await ult.edit("OK FUCKER")
 await ult.edit("OK BITCH")
 await ult.edit("OK GAY")
 await ult.edit("OK SIR")
 await ult.edit("OK MADAM")
 await ult.edit("OK BOSS! 😇")
  
  

@beast.on(beastx_cmd(pattern="pprank"))
async def pprank(ult):
    if not ult.text[0].isalpha() and ult.text[0] not in ("/", "#", "@", "!"):
        await ult.edit("PROMOTING USER..*")
        await asyncio.sleep(1)
        await ult.edit("PROMOTING USER...")
        await asyncio.sleep(1)
        await ult.edit("GIVING RIGHTS")
        await asyncio.sleep(1)
        await ult.edit("PROMOTED USER SUCCESSFULLY")
  
  
  
  
  
  
  
  
  
  
