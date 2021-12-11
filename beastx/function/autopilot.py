

from .. import beast,sedmrunal,sedprint 
from var import Var
from telethon.errors.rpcerrorlist import ChannelsTooMuchError
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

async def autopilot():

    chat_id = Var.BOTLOG_CHATID 
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    try:
      oo = await beast.get_me()
      await beast(EditAdminRequest(chat_id, oo.me.username, rights, "Assistant"))
      photo = await download_file(
        "https://telegra.ph/file/1da0b3ea529f74df23f1d.jpg", "channelphoto.jpg"
    )
      
      ll = await beast.upload_file(photo)
      await beast(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
      os.remove(photo)
      except noiceson:
        sedprint.info(
            "nice you have alreqady added bot in chat"
        )
        exit(1)

