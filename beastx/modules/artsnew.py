import asyncio
import os
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from . import *
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.ded$")
@beast.on(admin_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.edit(n + " ==             |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
K = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - -\n"
"_/﹋\_\n")
G = ("........___________________\n"
"....../ `-___________--_____|] - - - - - -\n"" - - ░ ▒▓▓█D \n"
"...../==o;;;;;;;;______.:/\n"
".....), -.(_(__) /\n"
"....// (..) ), —\n"
"...//___//\n")
D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
H = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")
E = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")


@beast.on(admin_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await monster.edit(M)
@beast.on(admin_cmd(pattern=r"pig"))
async def bluedevilpig(pig):
    await pig.edit(P)
@beast.on(admin_cmd(pattern=r"kiler"))
async def bluedevilkiller(kiler):
    await kiler.edit(K)
@beast.on(admin_cmd(pattern=r"gun"))
async def bluedevilgun(gun):
    await gun.edit(G)
@beast.on(admin_cmd(pattern=r"dog"))
async def bluedevildog(dog):
    await dog.edit(D)    
@beast.on(admin_cmd(pattern=r"hello"))
async def bluedevilhello(hello):
    await hello.edit(H)
@beast.on(admin_cmd(pattern=r"hmf"))
async def bluedevilhmf(hmf):
    await hmf.edit(E)
