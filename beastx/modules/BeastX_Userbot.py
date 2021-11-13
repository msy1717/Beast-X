from . import *

tgbotusername = Var.TG_BOT_USER_NAME_BF_HER

from beastx import ALIVE_NAME, CMD_LIST, lang

from beastx.utils import beastx_cmd

from beastx import beast

@beast_cmd(pattern=".repo ?(.*)")

async def repohand(event):

    results = await beast.inline_query(tgbotusername,'repo')

    await results[0].click(event.chat_id)
