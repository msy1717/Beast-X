 
#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made
import datetime
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
from telethon import events
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
from telethon.errors.rpcerrorlist import YouBlockedUserError
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
from telethon.tl.functions.account import UpdateNotifySettingsRequest
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
from beastx.utils import admin_cmd
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
from beastx import bot as javes
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
@javes.on(admin_cmd(pattern="history ?(.*)"))
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    chat = "Sangmatainfo_bot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              #Fixed By @Shivam_Patel
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              await conv.send_message("/search_id {}".format(sender))#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              #team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
              response1 = await response1 #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              response2 = await response2 #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
              response3= await response3 #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
          except YouBlockedUserError: 
              await event.reply("```Please unblock (@Sangmatainfo_bot) ```")
              #team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
              return
          if response1.text.startswith("No records found"):
             #team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
             await event.edit("```User never changed his Username...```")
             #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
          else: 
             await event.delete()
             #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
             await event.client.send_message(event.chat_id, response1.message)
             #team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
             await event.client.send_message(event.chat_id, response2.message)
             #team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates 
             await event.client.send_message(event.chat_id, response3.message)
             #team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam
#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam


#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@Godmrunal @Copyless786#team mates @danish_00,@Shivam_Patel,@xditya,@The_Siddharth_Nigam


# Credits Are Necessary Cause Bot Like Hellbot Can't Kang As they Have Kanged Our _inlinebot back and open buttons which for dc ME (@Shivam_Patel) made
