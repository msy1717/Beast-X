import os
from time import sleep
from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

banner = """
© Beast-X Userbot
• The Safest Userbot •
"""

info = "Get your API_ID and API_HASH from https://my.telegram.org\n\n"

def spinner():
    print("Checking Setup Telethon...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)

os.system("clear")
print(banner)
print(info)

try:
    API_ID = int(input("Please enter your API ID: \n"))
    API_HASH = input("Please enter your API HASH: \n")
except ValueError:
    print("❌ Wrong combination of API_ID / API_HASH")
    exit(0)

try:
    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("Generating a session for Beast-X...")

        string = client.session.save()

        # send the string to Saved Messages
        client.send_message(
            "me",
            f"🏝️ Beast-X Userbot ✨\n\n"
            f"`{string}`\n\n"
            "**⚠️ Do not share this string with anyone!**"
        )

        client.send_message(
            "me",
            "✅ The above is your `STRING_SESSION` for BeastX.\n\n"
            "__Thanks for using BeastX ❤️__\n\n"
            "• Join our channels ~ @BeastX_Bots / @BeastX_Userbot"
        )

        print("🎉 Session generated successfully! Check your Telegram Saved Messages.")

except ApiIdInvalidError:
    print("❌ Your API ID / API HASH combination is invalid. Kindly recheck.\nQuitting...")
    exit(0)
except ValueError:
    print("❌ API HASH must not be empty!\nQuitting...")
    exit(0)
except PhoneNumberInvalidError:
    print("❌ The phone number is invalid!\nQuitting...")
    exit(0)
