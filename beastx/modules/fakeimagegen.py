import os

import requests
from . import *

# hmm
@beast.on(beastx_cmd(pattern="picgen"))
@beast.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    if response.status_code == 200:
        with open("JUSTbeast.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By beast-X.\nGet Your Own Superpowers From [beast-X](github.com/TeamEviral/beast-X)."
    fole = "JUSTbeast.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/beastbot/JUSTbeast.jpg ")


CMD_HELP.update(
    {
        "picgen": "**Fake Picture Gen**\
\n\n**Syntax : **`.picgen`\
\n**Usage :** Genetates Fake Image.\
\n\n**Note : **The Person In Picture Really Doesn't Exist."
    }
)
