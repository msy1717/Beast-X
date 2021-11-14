import os
#MADE BY SHIVAM DONT KANG
import cv2
from beastx import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from beastx.utils import admin_cmd
from beastx import bot 
from beastx import bot as borg
import os , shutil


@borg.on(admin_cmd(pattern=r"gpic"))
async def hmm(event):

    await event.delete()
    linc = event.text
    links=linc[6:]
    text1,colors,text2=links.split("|")
    a,b,c=colors.split(";")
    window_name = 'Made By Shivam'
    image = cv2.imread("google.jpg") 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org1 = (255,65)
    org2 = (450,280)
    color = (int(a),int(b),int(c))
    thickness=2
    fontScale=1
    image = cv2.putText(image, text1, org1, font, fontScale,  
                 color, thickness, cv2.LINE_AA)
    cv2.imwrite("s_h_1_v_a_m_s.jpg", image)
    image = cv2.imread("s_h_1_v_a_m_s.jpg")
    image = cv2.putText(image, text2, org2, font, fontScale,  
                 color, thickness, cv2.LINE_AA)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_1_v_a_m.jpg", image)
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_1_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove("s_h_1_v_a_m.jpg")
    os.remove("s_h_1_v_a_m_s.jpg")

#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG
@borg.on(admin_cmd(pattern=r"fpic"))
async def hmm(event):

    await event.delete()
    linc = event.text
    links=linc[6:]
    text1,colors1,text2,colors2=links.split("|")
    a,b,c=colors1.split(";")
    d,e,f=colors2.split(";")
    window_name = 'Made By Shivam'
    image = cv2.imread("google.jpg") 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org1 = (255,65)
    org2 = (450,280)
    color1 = (int(a),int(b),int(c))
    color2 = (int(d),int(e),int(f))
    thickness=2
    fontScale=1
    image = cv2.putText(image, text1, org1, font, fontScale,  
                 color1, thickness, cv2.LINE_AA)
    cv2.imwrite("s_h_1_v_a_m_s.jpg", image)
    image = cv2.imread("s_h_1_v_a_m_s.jpg")
    image = cv2.putText(image, text2, org2, font, fontScale,  
                 color2, thickness, cv2.LINE_AA)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_1_v_a_m.jpg", image)
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_1_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove("s_h_1_v_a_m.jpg")
    os.remove("s_h_1_v_a_m_s.jpg")
CMD_HELP.update({"fakegooglesearch":"\n\n.gpic text1|no1;no2;no3|text2 \n\n.fpic text1|no1;no2;no3|text2|no1;no2;no3"})
#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG
