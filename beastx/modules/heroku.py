import os
import asyncio
import requests
import aiohttp
import math
import heroku3
fallback = None
from operator import itemgetter
from beastx import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID)
from beastx.utils import register as beast_cmd
from beastx import beast
from beastx.utils import admin_cmd

heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
useragent = (
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/81.0.4044.117 Mobile Safari/537.36'
)


FULL_SUDO = os.environ.get("FULL_SUDO", None)

@beast_cmd(outgoing=True, pattern=r"^!(set|get|del) var(?: |$)(.*)(?: |$)")
async def variable(var):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)                         
        app = Heroku.app(HEROKU_APP_NAME)
    except:
  	  return await var.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:"
                              "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        await var.edit("`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            val = var.pattern_match.group(2).split()[0]
            if val in heroku_var:
                return await var.edit(                    
                        "**Config Variable**:\n"
                        f"`{val}`\n"
                        "**Value**:\n"
                        f"`{heroku_var[val]}`\n"
                    )
            else:
                return await var.edit("**Config vars**:"
                                      f"\n\n`Error -> {val} not exists`")
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await var.edit("`[HEROKU]` variables:\n\n"
                                   "================================"
                                   f"\n```{result}```\n"
                                   "================================"
                                   )
            os.remove("configs.json")
            return
    elif exe == "set":
        await var.edit("`Setting information...`")
        val = var.pattern_match.group(2).split()
        try:
            val[1]
        except IndexError:
            return await var.edit("`!set var <config name> <value>`")
        await asyncio.sleep(1.5)
        if val[0] in heroku_var:
            await var.edit(
                      "**Successfully changed **\n"
                      "**Var**:\n"
                    f"`{val[0]}`\n"
                    "**Value**:\n"
                    f"`{val[1]}`\n"
                    "**Restarting...**"
                )            
        else:
            await var.edit(
                      "**Successfully added **\n"
                      "**Var**:\n"
                    f"`{val[0]}`\n"
                    "**Value**:\n"
                    f"`{val[1]}`\n"
                    "**Restarting...**"
                )            
        heroku_var[val[0]] = val[1]
    elif exe == "del":
        await var.edit("`Getting information to deleting vars...`")
        try:
            val = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await var.edit("`Please specify config vars you want to delete`")
        await asyncio.sleep(1.5)
        if val in heroku_var:
            await var.edit(f"**{val}**  `successfully deleted`\n Restarting......")
            del heroku_var[val]
        else:
            return await var.edit(f"**{val}**  `is not exists`")



@beast.on(admin_cmd(pattern=f"(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", allow_sudo=True))
async def variable(var):
  try:
     Heroku = heroku3.from_key(HEROKU_API_KEY)                         
     app = Heroku.app(HEROKU_APP_NAME)
  except:
  	return await var.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
  if not FULL_SUDO:
      await var.reply(f"`{A_NAME}:` **Sorry , Normal Sudo cant acess this comand,  active advance sudo by set  FULL_SUDO as true in heroku var**") 
  else:
    """
        Manage most of ConfigVars setting, set new var, get current var,
        or delete var...
    """
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:"
                              "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        rk = await var.reply("`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            val = var.pattern_match.group(2).split()[0]
            if val in heroku_var:
                return await rk.edit(                    
                        "**Config Variable**:\n"
                        f"`{val}`\n"
                        "**Value**:\n"
                        f"`{heroku_var[val]}`\n"
                    )
            else:
                return await rk.edit("**Config vars**:"
                                      f"\n\n`Error -> {val} not exists`")
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await rk.edit("`[HEROKU]` variables:\n\n"
                                   "================================"
                                   f"\n```{result}```\n"
                                   "================================"
                                   )
            os.remove("configs.json")
            return
    elif exe == "set":
        rk = await var.reply("`Setting information...`")
        val = var.pattern_match.group(2).split()
        try:
            val[1]
        except IndexError:
            return await rk.edit("`!set var <config name> <value>`")
        await asyncio.sleep(1.5)
        if val[0] in heroku_var:
            await rk.edit(
                      "**Successfully changed **\n"
                      "**Var**:\n"
                    f"`{val[0]}`\n"
                    "**Value**:\n"
                    f"`{val[1]}`\n"
                    "**Restarting...**"
                )            
        else:
            await rk.edit(
                      "**Successfully added **\n"
                      "**Var**:\n"
                    f"`{val[0]}`\n"
                    "**Value**:\n"
                    f"`{val[1]}`\n"
                    "**Restarting...**"
                )            
        heroku_var[val[0]] = val[1]
    elif exe == "del":
        rk = await var.reply("`Getting information to deleting vars...`")
        try:
            val = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await rk.edit("`Please specify config vars you want to delete`")
        await asyncio.sleep(1.5)
        if val in heroku_var:
            await rk.edit(f"**{val}**  `successfully deleted`\n Restarting......")
            del heroku_var[val]
        else:
            return await rk.edit(f"**{val}**  `is not exists`")



@beast_cmd(outgoing=True, pattern="^\.usage$")
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        headers = {
            'User-Agent': useragent,
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
        }
        await dyno.edit("`Getting usage......`")
        user_id = []
        user_id.append(heroku.account().id)
        if fallback is not None:
            user_id.append(fallback.account().id)
        msg = ''
        for aydi in user_id:
            if fallback is not None and fallback.account().id == aydi:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY_FALLBACK}'
            else:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY}'
            path = "/accounts/" + aydi + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                await dyno.edit("`Cannot get information...`")
                continue
            result = r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - Used per/App Usage - """
            Apps = result['apps']
            """ - Sort from larger usage to lower usage - """
            Apps = sorted(Apps, key=itemgetter('quota_used'), reverse=True)
            if fallback is not None and fallback.account().id == aydi:
                apps = fallback.apps()
                msg += "**Dyno Usage fallback-account**:\n\n"
            else:
                apps = heroku.apps()
                msg += "**Dyno Usage **:\n\n"
            try:
                Apps[0]
            except IndexError:
                """ - If all apps usage are zero - """
                for App in apps:
                    msg += (
                        f" ~>> `Dyno usage for`  **App**:\n"
                        f"     •  `0`**h**  `0`**m**  "
                        f"**|**  [`0`**%**]\n\n"
                    )
            for App in Apps:
                AppName = '__~~Deleted or transferred app~~__'
                ID = App.get('app_uuid')
                try:
                    AppQuota = App.get('quota_used')
                    AppQuotaUsed = AppQuota / 60
                    AppPercentage = math.floor(AppQuota * 100 / quota)
                except IndexError:
                    AppQuotaUsed = 0
                    AppPercentage = 0
                finally:
                    AppHours = math.floor(AppQuotaUsed / 60)
                    AppMinutes = math.floor(AppQuotaUsed % 60)
                    for names in apps:
                        if ID == names.id:
                            AppName = f"**{names.name}**"
                            break
                    msg += (
                        f" ~>> `Dyno usage for`  App:\n"
                        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
                        f"**|**  [`{AppPercentage}`**%**]\n\n"
                    )
            msg = (
                f"{msg}"
                " ~>> `Dyno hours quota remaining this month`:\n"
                f"     •  `{hours}`**h**  `{minutes}`**m**  "
                f"**|**  [`{percentage}`**%**]\n\n"
            )
        if msg:
            return await dyno.edit(msg)
        else:
            return


@beast.on(admin_cmd(pattern=f"usage$", allow_sudo=True))
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        headers = {
            'User-Agent': useragent,
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
        }
        rk = await dyno.reply("`Getting usage......`")
        user_id = []
        user_id.append(heroku.account().id)
        if fallback is not None:
            user_id.append(fallback.account().id)
        msg = ''
        for aydi in user_id:
            if fallback is not None and fallback.account().id == aydi:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY_FALLBACK}'
            else:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY}'
            path = "/accounts/" + aydi + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                await rk.edit("`Cannot get information...`")
                continue
            result = r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - Used per/App Usage - """
            Apps = result['apps']
            """ - Sort from larger usage to lower usage - """
            Apps = sorted(Apps, key=itemgetter('quota_used'), reverse=True)
            if fallback is not None and fallback.account().id == aydi:
                apps = fallback.apps()
                msg += "**Dyno Usage fallback-account**:\n\n"
            else:
                apps = heroku.apps()
                msg += "**Dyno Usage **:\n\n"
            try:
                Apps[0]
            except IndexError:
                """ - If all apps usage are zero - """
                for App in apps:
                    msg += (
                        f" ~>> `Dyno usage for`  **App**:\n"
                        f"     •  `0`**h**  `0`**m**  "
                        f"**|**  [`0`**%**]\n\n"
                    )
            for App in Apps:
                AppName = '__~~Deleted or transferred app~~__'
                ID = App.get('app_uuid')
                try:
                    AppQuota = App.get('quota_used')
                    AppQuotaUsed = AppQuota / 60
                    AppPercentage = math.floor(AppQuota * 100 / quota)
                except IndexError:
                    AppQuotaUsed = 0
                    AppPercentage = 0
                finally:
                    AppHours = math.floor(AppQuotaUsed / 60)
                    AppMinutes = math.floor(AppQuotaUsed % 60)
                    for names in apps:
                        if ID == names.id:
                            AppName = f"**{names.name}**"
                            break
                    msg += (
                        f" ~>> `Dyno usage for`  App:\n"
                        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
                        f"**|**  [`{AppPercentage}`**%**]\n\n"
                    )
            msg = (
                f"{msg}"
                " ~>> `Dyno hours quota remaining this month`:\n"
                f"     •  `{hours}`**h**  `{minutes}`**m**  "
                f"**|**  [`{percentage}`**%**]\n\n"
            )
        if msg:
            return await rk.edit(msg)
        else:
            return




@beast_cmd(outgoing=True, pattern="^\!shutdown$")
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        app.scale_formation_process("worker", 0)
        text = f"`Turning Off Dynos` "
        sleep = 1
        dot = "."
        while (sleep <= 3):
            await dyno.edit(text + f"`{dot}`")
            await asyncio.sleep(1)
            dot += "."
            sleep += 1
        await dyno.respond(f"turned off...`")
        return await dyno.delete()
        


@beast.on(admin_cmd(pattern=f"shutdown$", allow_sudo=True))
async def _(dyno):        
  try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
  except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
  if not FULL_SUDO:
      await dyno.reply(f"`{JAVES_NNAME}:` **Sorry , Normal Sudo cant acess this comand,  active advance sudo by set  FULL_SUDO as true in heroku var**") 
  else:  	  
        app.scale_formation_process("worker", 0)
        text = f"`Turning Off Dynos` "
        sleep = 1
        dot = "."
        while (sleep <= 3):
            await dyno.reply(text + f"`{dot}`")
            await asyncio.sleep(1)
            dot += "."
            sleep += 1
        await dyno.respond(f"turned off...`")
        return await dyno.delete()        
        
        
        
@beast_cmd(outgoing=True, pattern="^\!logs$")
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        await dyno.edit("`Getting Logs....`")
        with open('logs.txt', 'w') as log:
            log.write(app.get_log())
        await dyno.client.send_file(
            dyno.chat_id,
            "logs.txt",
            reply_to=dyno.id,
            caption="`logs of 100+ lines`",
        )
        await dyno.edit("`Sending.......`")
        await asyncio.sleep(5)
        await dyno.delete()
        return os.remove('logs.txt')



@beast.on(admin_cmd(pattern=f"logs$", allow_sudo=True))
async def _(dyno):        
  try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
  except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
  if not FULL_SUDO:
      await dyno.reply(" **Sorry , Normal Sudo cant acess this comand,  active advance sudo by set  FULL_SUDO as true in heroku var**") 
  else:        
        rk = await dyno.reply("`Getting Logs....`")
        with open('logs.txt', 'w') as log:
            log.write(app.get_log())
        await dyno.client.send_file(
            dyno.chat_id,
            "logs.txt",
            reply_to=dyno.id,
            caption="`logs of 100+ lines`",
        )
        rk = await rk.edit("`Sending.......`")
        await asyncio.sleep(5)
        return os.remove('logs.txt')

@beast_cmd(outgoing=True, pattern="^\!restart$")
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        try:           
            Dyno = app.dynos()[0]
        except IndexError:
            return await dyno.respond(f"**{HEROKU_APP_NAME}** `is not on...`")
        else:
            text = f"`Restarted Dynos....`"
            Dyno.restart()
            sleep = 1
            dot = "."
            await dyno.edit(text)
            while (sleep <= 24):
                await dyno.edit(text + f"`{dot}`")
                await asyncio.sleep(1)
                if len(dot) == 3:
                    dot = "."
                else:
                    dot += "."
                sleep += 1
            state = Dyno.state
            if state == "up":
                await dyno.respond(f"**{HEROKU_APP_NAME}** `restarted...`")
            elif state == "crashed":
                await dyno.respond(f"**{HEROKU_APP_NAME}** `crashed...`")
            return await dyno.delete()
            

@beast.on(admin_cmd(pattern=f"restart$", allow_sudo=True))
async def _(dyno):        
  try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
  except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
  if not FULL_SUDO:
      await dyno.reply(" **Sorry , Normal Sudo cant acess this comand,  active advance sudo by set  FULL_SUDO as true in heroku var**") 
  else:                
        try:           
            Dyno = app.dynos()[0]
        except IndexError:
            return await dyno.respond(f"**{HEROKU_APP_NAME}** `is not on...`")
        else:
            text = f"`Restarting Dynos....`"
            Dyno.restart()
            sleep = 1
            dot = "."
            rk = await dyno.reply(text)
            while (sleep <= 24):
                await rk.edit(text + f"`{dot}`")
                await asyncio.sleep(1)
                if len(dot) == 3:
                    dot = "."
                else:
                    dot += "."
                sleep += 1
            state = Dyno.state
            if state == "up":
                await dyno.respond(f"**{HEROKU_APP_NAME}** `restarted...`")
            elif state == "crashed":
                await dyno.respond(f"**{HEROKU_APP_NAME}** `crashed...`")
            return await dyno.delete()
            





CMD_HELP.update({
    "heroku":
    "** heroku apikey, name must set correctly for use this commands get help from https://telegra.ph/RkPavi-06-09-6** "
    "\n\n`!usage`"
    "\nUsage: Check your heroku dyno hours remaining"
    "\n\n`!set var <NEW VAR> <VALUE>`"
    "\nUsage: add new variable or update existing value variable"
    "\nAfter setting a variable the bot will restarted"
    "\n\n`!get var or !get var <VAR>`"
    "\nUsage: get your existing varibles, use it only on your private group!"
    "\nThis returns all of your private information, please be caution..."
    "\n\n`!del var <VAR>`"
    "\nUsage: delete existing variable"
    "\n After deleting variable the bot will restarted"
    "\n\n`!logs <VAR>`"
    "\nUsage: get herolu logs"
    "\n\n`!restart <VAR>`"
    "\nUsage: Restart Dynos"
    "\n\n`!shutdown <VAR>`"
    "\nUsage: off dynos, It will shutdown your javes"
    "\n\n**Sudo commands type !help sudo for more info **"
    "\n.restart , .shutdown , .logs , .set/get/del var , .usage"    
})
