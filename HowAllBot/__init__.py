import os
import logging
import time
from pyrogram import Client, filters, errors

StartTime = time.time()
logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__)

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

pbot = Client("HowAllBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
me = pbot.get_me()
BOT_USERNAME = me.username
# Credits Logger
print(
    f"[{BOT_USERNAME}] How-All-Bot Is Starting. | Aasf • Cyber • King • Project | Licensed Under GPLv3."
)
print(f"[{BOT_USERNAME}] Project Maintained By: github.com/AASFCYBERKING (t.me/AASF_CYBERKING)")

print(f"[{BOT_USERNAME}] Is Alive")
