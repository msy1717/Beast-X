from faker import Faker as dc

from beastx import bot as beast

from ..utils import admin_cmd as wtf

from . import *
@beast.on(wtf("card"))
async def _beastt(bst):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await bst.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{chris}`")
