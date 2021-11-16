from datetime import datetime


from . import *
@beast.on(beastx_cmd("time ?(.*)"))  # pylint:disable=E0602
async def gn(event):
    if event.fwd_from:
        return
    current_time = datetime.now().strftime(
        "CURRENT DATE & TIME \nLOCATION: India \nTime: %H:%M:%S \nDate: %d.%m.%y"
    )
    datetime.now()
    input_str = event.pattern_match.group(1)
    event.message.id
    if input_str:
        current_time = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message.id
    await edit_or_reply(
        event,
        current_time,
    )
