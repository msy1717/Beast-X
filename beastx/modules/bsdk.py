#plugin by @e3ris
#ported to FireX bot by @Godmrunal

import random
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from beastx import ALIVE_NAME, CMD_HELP
from . import *
"""
✘ Commands Available -
• .bsdk
    send random gallli to cha.
"""

bsdk = ["Phatele Nirodh Ke Natije!","Chut Ka Maindak…","Abla Naari, Tere Bable Bhaari…","Chut Ke Pasine Mein Talay Hue Bhajiye…","Chullu Bhar Muth Mein Doob Mar!","Kaali Chut Ke Safed Jhaant…","Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain…","Naa Chut, Naa Choche, Aur Nakhre Noor Jahan Ke!","Teri Gaand Mein Kutte Ka Lund…","Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!"]
@beast.on(admin_cmd(pattern="bsdk$"))
async def thanks(ult):
  b = random.choice(bsdk)
  return await ult.edit(b)

CMD_HELP.update(
    {
        "BSDK": """Plugin : bsdk
        
Commands in animation1 are 
  •  .bsdk
 
Function : **send random gallli to chat"""
    }
)
