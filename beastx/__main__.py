import logging
from pathlib import Path
from sys import argv
import var

import telethon.utils
from telethon import TelegramClient

from var import Var
from beastx import bot
from beastx.Configs import Config
from telethon.tl.functions.messages import AddChatUserRequest
from beastx.utils import load_module, start_assistant
botusername = Var.TG_BOT_USER_NAME_BF_HER
chattt_id = Var.PRIVATE_GROUP_ID
try:
    redis_info = REDIS_URI.split(':')
    udB = redis.StrictRedis(
    host=redis_info[0],
    port=redis_info[1],
    password=REDIS_PASSWORD,
    charset="utf-8",
    decode_responses=True)
except Exception as e:
    print("Database errors! Recheck REDIS_URI and REDIS_PASSWORD!!")
    print(str(e))
    print("Bot is quiting...")
    exit()



sed = logging.getLogger("beastx")

async def autobot():
    if Var.get("BOT_TOKEN"):
        return
    if Var.TG_BOT_TOKEN_BF_HER:
        return udB.set("BOT_TOKEN", Var.BOT_TOKEN)
    await bot.start()
    LOGS.info("MAKING A TELEGRAM BOT FOR YOU AT @BotFather, Kindly Wait")
    who = bot.me
    name = who.OWNER_NAME + "'s Assistant Bot"
    if who.username:
        username = who.username + "_bot"
    else:
        username = "ultroid_" + (str(who.id))[5:] + "_bot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        sed.info(
            "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
        )
        exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            sed.info(
                "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
            )
            exit(1)
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "ultroid_" + (str(who.id))[6:] + str(ran) + "_bot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            udB.set("BOT_TOKEN", token)
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            sed.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
        else:
            sed.info(
                "Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
            )

            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        udB.set("BOT_TOKEN", token)
        await ultroid_bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await ultroid_bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await ultroid_bot.send_message(bf, "Search")
        sed.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
    else:
        sed.info(
            "Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
        )

        exit(1)


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_TOKEN is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
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
    sed.info("---------------------------------------")
    sed.info("------------@BeastX_Userbot------------")
    sed.info("---------------------------------------")
           
else:
    sed.info("beastx Has Been Installed Sucessfully !")
    sed.info("Hope you will enjoy")
    

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
