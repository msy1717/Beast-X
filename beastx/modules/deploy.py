from . import *
@beast.on(admin_cmd(pattern=r"deployme"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Click Here to deploy My Bot](https://heroku.com/deploy?template=https://github.com/msy1717/Beast-X/blob/main)")
