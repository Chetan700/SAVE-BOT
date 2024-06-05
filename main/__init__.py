#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("20168891", default=None, cast=int)
API_HASH = config("445779f3b1dab02b39614db1bb089b87", default=None)
BOT_TOKEN = config("7240350465:AAExHtNXW18wWs9zJHu0CvcSpw05W3X8Xx0", default=None)
SESSION = config("AgBwnYIAEDZmvzufxDz-nXr18_LpYRcU3Li6WJ7o_w-1ga2X2ZXQKnGQ8rm5QEnUVwOMXs0FZ_BNT2uVVjbmuQpzO00QXRq4CW5TqpNXWrP3KvgtA3394AWZfgAYAOdfuBE1yobxwvqo4OfwEpnlJE47iK1_j40ip8sM6SRBhf0ZOacXFKvpmturNzyEs9OGuuvm7WV1Bb7XuMzkTw18WcDZwrHYtCwXMO8iFzQcO3IagR3Fpn1sLP_7GXy5zBzO_cc7I3WSO0Rh-VomKmgWrlSZiK8qAtTOTmP91a4FcAfC9RSL5ZxV3SRgABLWIQj_3uAyxLcuuj9jkJZDTeAiWOHffrx7OQAAAABwiFjpAA", default=None)
FORCESUB = config("php83", default=None)
AUTH = config("5768175071", default=None, cast=int)

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
