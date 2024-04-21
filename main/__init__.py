#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
#API_ID = config("API_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
#SESSION = config("SESSION", default=None)
#FORCESUB = config("FORCESUB", default=None)
#AUTH = config("AUTH", default=None, cast=int)

API_ID=23476439
API_HASH="1626e884119a29dbccbb78e39b48128f"
BOT_TOKEN="7079929259:AAEC6jQzSzAPolYhL4nwExldNlIKf4sRcjU"
SESSION="
BQEDKZgAlnJHauRnpOhFry9WVo4CVGaaFHhirizMnvwciqkgjGRXKdX_tZ-7_6NAr-Ysb-vOl2xCMX2owrJOCIDXQVh_pAuOJQI15iMVBYel3jXmurhTPwcp39cGlX8Av8iF8xRyqrRjnx1vm42h1hUFXnd-6y-rOvid91Z4BdNCJR4mTwJgB5gA6GPwt4qDf2NRp01WsTE_TpVnfBvyiPVXXTxU1VIjrT6HprxUnG9qKeCxgqJ7S-_-u6efBytwFwah9WLccVC3XBTad0CcbXXaFLCoVQonGDU0DgCO42mQ3TZIWmgss84SNb6sAiexEQi3vNCC3LrG7sewESPqRAsfor_DuAAAAAFQUsvEAA"
FORCESUB="MehulBots"
AUTH=5434500969

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
