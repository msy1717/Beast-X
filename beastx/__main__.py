import logging
from pathlib import Path
from sys import argv
import var

import telethon.utils
from telethon import TelegramClient

from var import Var
from beastx import bot
from beastx.Configs import Config
from beastx.utils import load_module, start_assistant

sed = logging.getLogger("beastx")
hmm = '''
 ____                 _    __  __
| __ )  ___  __ _ ___| |_  \ \/ /
|  _ \ / _ \/ _` / __| __|  \  / 
| |_) |  __/ (_| \__ \ |_   /  \ 
|____/ \___|\__,_|___/\__| /_/\_\
'''


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


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
    sed.info(hmm)
else:
    sed.info("beastx Has Been Installed Sucessfully !")
    sed.info("Hope you will enjoy")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
