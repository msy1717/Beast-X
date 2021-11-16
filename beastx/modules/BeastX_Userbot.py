from . import *

tgbotusername = Var.TG_BOT_USER_NAME_BF_HER

from beastx import ALIVE_NAME, CMD_LIST, lang




#@beast_cmd(pattern=".repo ?(.*)")

#async def repohand(event):

   # results = await beast.inline_query(tgbotusername,'repo')

    #await results[0].click(event.chat_id)
@beast_cmd(outgoing=True, pattern="^.repo$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Hello , User I Am Using [BeastXUserbot](https://github.com/msy1717/Beast-X) ! Worth A Try 😌")
			  
            
            
 #sed----------------------------------------------------------------------------------------
