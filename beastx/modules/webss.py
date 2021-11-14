# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
#PORTED TO JAVES BY SH1VAM
import asyncio
import os
from re import match

import aiofiles
from selenium import webdriver
from beastx import bot as javes
from beastx import CMD_HELP
from beastx.javes_main.heroku_var import Config
from beastx.utils import admin_cmd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@javes.on(admin_cmd("webss (.*)"))
async def webss(message):
    king= message.text
    amaan=king[7:]
    link_match = match(r"\bhttps?://.*\.\S+", amaan)
    if not link_match:
        await message.edit("`I need a valid link to take screenshots from.`")
        return
    link = link_match.group()
    await message.edit("`Processing ...`")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome((ChromeDriverManager().install()),chrome_options=chrome_options)
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await message.edit(
        f"`Generating screenshot of the page...`"
        f"\n`Height of page = {height}px`"
        f"\n`Width of page = {width}px`"
        f"\n`Waiting ({int(wait_for)}s) for the page to load.`"
    )
    await asyncio.sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    driver.close()
    message_id = message.message.id
    reply = await message.get_reply_message()
    if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
    file_path = os.path.join(Config.TEMP_DOWNLOAD_DIRECTORY , "webss.png")
    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(im_png)
    await asyncio.gather(
        message.delete(),
        message.client.send_file(
            message.chat_id,
            file_path,
            caption=link,
            force_document=False,
            reply_to=message_id,
        ),
    )
    os.remove(file_path)
    driver.quit()

CMD_HELP.update({"Webss":"\n\n.webss link "})
