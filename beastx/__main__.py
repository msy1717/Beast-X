import logging
from pathlib import Path
from sys import argv
import var
import telethon.utils
from telethon import TelegramClient
from telethon import events
import os
from var import Var
from . import beast  
from beastx.Configs import Config
from telethon.tl.functions.messages import AddChatUserRequest
from beastx.utils import load_module, start_assistant
import asyncio
from . import bot,sedmrunal

#rom . import semxx,semxxx


sur = Config.PRIVATE_GROUP_ID

UL = Config.TG_BOT_USER_NAME_BF_HER

chat_id = sur
MSG = f"""
✨𝔹𝕖𝕒𝕤𝕥 ℍ𝕒𝕤 𝔹𝕖𝕖𝕟 𝔻𝕖𝕡𝕝𝕠𝕪𝕖𝕕!

            ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎

┏━━━━━━━━━━━━━━━━━━

┣•Assistant➠ @{UL}

┣•User➠ @

┣•Support➠ @BeastX_Support

┗━━━━━━━━━━━━━━━━━━

Do `.ping `or` /alive` for check userbot working

"""


sed = logging.getLogger("beastx")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
    await sedmrunal.send_message(sur, MSG)
    

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
        
import glob
'''if Config.EXTRA_PLUGS == "ENABLE":
    os.system("git clone https://github.com/ULTRA-OP/ULTRA_PLUGS.git ./beastx/modules/")
    path = "beastx/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    sed.info('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:'''
        
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
