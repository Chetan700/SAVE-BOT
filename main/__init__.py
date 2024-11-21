#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23382015", default=None, cast=int)
API_HASH = config("2eaca0be3817a57f4f6f0b7671853316", default=None)
BOT_TOKEN = config("7687719017:AAHCNsc-cTYVNnAsdW__O8LVqFvpekFZhws", default=None)
SESSION = config("BQAf70YArgFzjwKb5PefA2aUO4YQ3Vn1RqelBYbWy52P69jnK14g1uBYtB6JvddF7zl4adakgoEug2bcwEVXFgdHxudu28x3aPH0-nxSvcH-r-CotA81Nn7-Cd68FAgimC4eCRMOAaKlUFncluXdbscuH-VzOtVNqlzCWRglN79p9UDzlnwSclGSUbO4xsFezDFswmrcgIJux9V4jzNKN9PtWvEAZfkyS-5D7Ca2ajtJ0i2-9RU5kCljJx8f9Mu0Uq9D5C2wTewIK1Xc3DpHHOxxrrFHqLAifOtNbZTGfII3uKz01otJeZMJO5IITy5R6d71e6m_dr1uAs9Yi7iwNKVFXsht6QAAAAFmwNdaAA", default=None)
FORCESUB = config("ruturajking", default=None)
AUTH = config("6018881370", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
