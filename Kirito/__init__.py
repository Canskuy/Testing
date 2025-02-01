import logging
import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# Ensure Python version is at least 3.6
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a Python version of at least 3.6! Bot quitting.")
    sys.exit(1)

# Load environment variables
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    LOGGER.error("Token bot tidak ditemukan. Harap periksa file .env atau environment variable.")
    sys.exit(1)

# Load other configurations
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

if not all([API_ID, API_HASH, STRING_SESSION]):
    LOGGER.error("API_ID, API_HASH, atau STRING_SESSION tidak valid. Harap periksa konfigurasi Anda.")
    sys.exit(1)

# Initialize TelegramClient
try:
    from telethon import TelegramClient
    from telethon.sessions import StringSession

    client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
    client.start()
    LOGGER.info("TelegramClient started successfully.")
except Exception as e:
    LOGGER.error(f"Failed to start TelegramClient: {e}")
    sys.exit(1)

# Initialize Pyrogram Client
try:
    from pyrogram import Client

    pbot = Client(
        ":memory:",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=TOKEN,
        workers=min(32, os.cpu_count() + 4),
    )
    apps = [pbot]
    LOGGER.info("Pyrogram Client initialized successfully.")
except Exception as e:
    LOGGER.error(f"Failed to initialize Pyrogram Client: {e}")
    sys.exit(1)

# Load handlers
def setup_handlers():
    from .modules.helper_funcs.handlers import (
        CustomCommandHandler,
        CustomMessageHandler,
        CustomRegexHandler,
    )
    import telegram.ext as tg
    tg.RegexHandler = CustomRegexHandler
    tg.CommandHandler = CustomCommandHandler
    tg.MessageHandler = CustomMessageHandler

setup_handlers()

__all__ = ["dispatcher", "updater", "LOGGER"]