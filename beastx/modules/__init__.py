from var import Var
from beastx.Configs import Config
from beastx.utils import beastx_cmd
from beastx import beast
from beastx.utils import register as beast_cmd
from telethon.tl.functions.users import GetFullUserRequest

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from beastx import CMD_HELP

#OWNER_ID = beast.me.id
#OWNER_NAME = beast.me.first_name

from bs4 import BeautifulSoup
from random import choice, randrange, shuffle




issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "2.0"
if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING Beast-X STATS ✘\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {amiusingsudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"HEROKU = {riplife} \n"
    f"G-DRIVE = {wearenoob}"
)
