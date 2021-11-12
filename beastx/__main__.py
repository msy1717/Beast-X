import logging
from pathlib import Path
from sys import argv
import var
import telethon.utils
from telethon import TelegramClient
from telethon import events,Button
import os
from var import Var
from . import beast  
from beastx.Configs import Config
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.users import GetFullUserRequest
from beastx.utils import load_module, start_assistant
import asyncio
from . import bot,sedmrunal
bot = beast
#rom . import semxx,semxxx
#####################################
plugin_channel = "@BeastX_Plugins" 
#####################################

sur = Config.PRIVATE_GROUP_ID

UL = Config.TG_BOT_USER_NAME_BF_HER

VR = "Beast 0.1"
chat_id = sur

MSG = f"""
✨𝔹𝕖𝕒𝕤𝕥 ℍ𝕒𝕤 𝔹𝕖𝕖𝕟 𝔻𝕖𝕡𝕝𝕠𝕪𝕖𝕕!

            ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎

┏━━━━━━━━━━━━━━━━━
┣•Assistant➠ {UL}
┣•Status➠ `Running`
┣•Version➠ {VR}
┗━━━━━━━━━━━━━━━━━

Do `.ping `or` /alive` for check userbot working

"""


sed = logging.getLogger("beastx")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
    await sedmrunal.send_message(sur, MSG,
                                 
                                  buttons=[

                        [Button.url("⭐Updates", url="https://t.me/BeastX_Userbot")],

                        [Button.url("⚡Support",url="https://t.me/BeastX_Support")]

                    ])

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
        
async def a():

  sed.info("Connecting...") ; 

  o = ""

  la = 0

  try:

     await bot.start() ; sed.info("beastx connected") ; o = "client"

  except:

    sed.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
import glob
async def a():
            test1 = await bot.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
            for ixo in total_doxx:
                        mxo = test1[ixo].id ; await bot.download_media(await bot.get_messages(client, ids=mxo), "beastx/modules/")
                        ar = glob.glob("beastx/modules/*.py")
                        f = len(ar)
                        sed.info(f" loading {f} modules it may take 1 minute please wait")
                        for i in ar:
                                    br = os.path.basename(i)
                                    cr = (os.path.splitext(br)[0])
                                    import_module(f"beastx.modules.{cr}")
                                    la += 1
                                    sed.info(f" loaded {la}/{f} modules")  

path = "beastx/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
 

        
if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "beastx/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("beastx And Assistant Bot Have Been Installed Successfully !")
    sed.info("---------------------------------------")
    sed.info("------------@BeastX_Userbot------------")
    sed.info("---------------------------------------")
           
else:
    sed.info("beastx Has Been Installed Sucessfully !")
    sed.info("Hope you will enjoy")
    



 #await bot.send_message(chat_id,MSG)
    
#else:
   # sed.info("your Get_Msg disable")
    
    

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
