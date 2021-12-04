import os

from time import sleep  

os.system("pip install -U telethon")

os.system("pip install --upgrade telethon")

import telethon 

from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError

from telethon.sessions import StringSession

from telethon.sync import TelegramClient

a = """

© Beast-X Userbot

• The Safest Userbot •

"""

x = "Get your API_ID, API_HASH get from my.telegram.org\n\n"

def spinner():

    print("Checking Setup Telethon...")

    for _ in range(3):

        for frame in r"-\|/-\|/":

            print("\b", frame, sep="", end="", flush=True)

            sleep(0.1)

        

os.system("clear")

 

print(a)

print(x)

try:

    API_ID = int(input("Please enter your API ID: \n"))

    API_HASH = input("Please enter your API HASH: \n")

except ValueError:

    print('Wrong combnation of API_ID, HASH')

    exit(0)

try:

        with TelegramClient(StringSession(), API_ID, API_HASH) as mrunal:

            print("Generating a session For Beast-X")

            bby = mrunal.send_message(

                "me",

                f"🏝️Beast X Userbot✨:\n\n`{mrunal.session.save()}`\n\n**Do not share this anywhere!**",

            )

            bby.reply("The Above is the your `STRING_SESSION`🤗 FOR your BeastX\n\n__Thanks For Using BeastX❤️__\n\n•Join our channels ~ @BeastX_Bots / @BeastX_Userbot")

            print(

                "Your SESSION has been generated. Check your telegram saved messages!"

            )

            exit(0)

except ApiIdInvalidError:

        print(

            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."

        )

        exit(0)

except ValueError:

        print("API HASH must not be empty!\nQuitting...")

        exit(0)

except PhoneNumberInvalidError:

        print("The phone number is invalid!\nQuitting...")

        exit(0)
