import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Debug: Cetak semua environment variable yang dimuat
print("Environment variables loaded from .env:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Ambil token dari environment variable
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("Token bot tidak ditemukan. Harap periksa file .env atau environment variable.")
    exit(1)

def get_user_list(config, key):
    """
    Get a list of users from a JSON file.
    """
    config_path = os.path.join(os.getcwd(), "KiritoRobot", config)
    if not os.path.exists(config_path):
        print(f"File {config} tidak ditemukan.")
        return []

    with open(config_path, "r") as json_file:
        return json.load(json_file)[key]

class Config:
    """
    Configuration class for the bot.
    """
    LOGGER = True

    # REQUIRED
    API_ID = int(os.getenv("API_ID", ""))  # Get API_ID from environment variable
    API_HASH = os.getenv("API_HASH", "")  # Get API_HASH from environment variable
    BOT_ID = os.getenv("BOT_ID", "")  # Get BOT_ID from environment variable
    TOKEN = os.getenv("TOKEN", "")  # Get TOKEN from environment variable
    OWNER_ID = int(os.getenv("OWNER_ID", ""))  # Get OWNER_ID from environment variable
    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "")  # Get OWNER_USERNAME from environment variable
    OPENWEATHERMAP_ID = os.getenv("OPENWEATHERMAP_ID", "22322")  # Default OpenWeatherMap ID
    BOT_USERNAME = os.getenv("BOT_USERNAME", "")  # Get BOT_USERNAME from environment variable
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")  # Get SUPPORT_CHAT from environment variable
    JOIN_LOGGER = int(os.getenv("JOIN_LOGGER", "-1001740507422"))  # Get JOIN_LOGGER from environment variable
    EVENT_LOGS = int(os.getenv("EVENT_LOGS", "-1001740507422"))  # Get EVENT_LOGS from environment variable

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "").replace("postgres://", "postgresql://", 1)
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")  # Get MONGO_DB_URI from environment variable
    STRING_SESSION = os.getenv("STRING_SESSION", "")  # Get STRING_SESSION from environment variable
    ARQ_API_KEY = os.getenv("ARQ_API_KEY", "")  # Get ARQ_API_KEY from environment variable
    ARQ_API_URL = os.getenv("ARQ_API_URL", "https://arq.hamker.in/")  # Default ARQ API URL
    LOAD = os.getenv("LOAD", "").split()  # Get LOAD from environment variable
    NO_LOAD = os.getenv("NO_LOAD", "rss cleaner connection math").split()  # Get NO_LOAD from environment variable
    WEBHOOK = bool(os.getenv("WEBHOOK", False))  # Get WEBHOOK from environment variable
    INFOPIC = bool(os.getenv("INFOPIC", True))  # Get INFOPIC from environment variable
    URL = os.getenv("URL", None)  # Get URL from environment variable
    SPAMWATCH_API = os.getenv("SPAMWATCH_API", "")  # Get SPAMWATCH_API from environment variable
    SPAMWATCH_SUPPORT_CHAT = os.getenv("SPAMWATCH_SUPPORT_CHAT", "SpamWatchSupport")  # Default SpamWatch support chat

    # OPTIONAL
    DRAGONS = get_user_list("elevated_users.json", "sudos")  # Get DRAGONS from JSON file
    DEV_USERS = get_user_list("elevated_users.json", "devs")  # Get DEV_USERS from JSON file
    DEMONS = get_user_list("elevated_users.json", "supports")  # Get DEMONS from JSON file
    TIGERS = get_user_list("elevated_users.json", "tigers")  # Get TIGERS from JSON file
    WOLVES = get_user_list("elevated_users.json", "whitelists")  # Get WOLVES from JSON file
    DONATION_LINK = os.getenv("DONATION_LINK", None)  # Get DONATION_LINK from environment variable
    CERT_PATH = os.getenv("CERT_PATH", None)  # Get CERT_PATH from environment variable
    PORT = int(os.getenv("PORT", 5000))  # Get PORT from environment variable
    DEL_CMDS = bool(os.getenv("DEL_CMDS", True))  # Get DEL_CMDS from environment variable
    STRICT_GBAN = bool(os.getenv("STRICT_GBAN", True))  # Get STRICT_GBAN from environment variable
    WORKERS = int(os.getenv("WORKERS", 8))  # Get WORKERS from environment variable
    BAN_STICKER = os.getenv("BAN_STICKER", "")  # Get BAN_STICKER from environment variable
    ALLOW_EXCL = bool(os.getenv("ALLOW_EXCL", True))  # Get ALLOW_EXCL from environment variable
    CASH_API_KEY = os.getenv("CASH_API_KEY", "awoo")  # Get CASH_API_KEY from environment variable
    TIME_API_KEY = os.getenv("TIME_API_KEY", "awoo")  # Get TIME_API_KEY from environment variable
    WALL_API = os.getenv("WALL_API", "awoo")  # Get WALL_API from environment variable
    AI_API_KEY = os.getenv("AI_API_KEY", "awoo")  # Get AI_API_KEY from environment variable
    BL_CHATS = os.getenv("BL_CHATS", "").split()  # Get BL_CHATS from environment variable
    SPAMMERS = os.getenv("SPAMMERS", None)  # Get SPAMMERS from environment variable
    ALLOW_CHATS = os.getenv("ALLOW_CHATS", None)  # Get ALLOW_CHATS from environment variable
    ERROR_LOGS = int(os.getenv("ERROR_LOGS", "-1001740507422"))  # Get ERROR_LOGS from environment variable
    TEMP_DOWNLOAD_DIRECTORY = os.getenv("TEMP_DOWNLOAD_DIRECTORY", "./")  # Get TEMP_DOWNLOAD_DIRECTORY from environment variable
    MONGO_DB = os.getenv("MONGO_DB", "KiritoRobot")  # Get MONGO_DB from environment variable
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))  # Get MONGO_PORT from environment variable
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "siap")  # Get HEROKU_APP_NAME from environment variable
    HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "YES")  # Get HEROKU_API_KEY from environment variable
    REM_BG_API_KEY = os.getenv("REM_BG_API_KEY", "yahoo")  # Get REM_BG_API_KEY from environment variable
    LASTFM_API_KEY = os.getenv("LASTFM_API_KEY", "yeah")  # Get LASTFM_API_KEY from environment variable
    CF_API_KEY = os.getenv("CF_API_KEY", "jk")  # Get CF_API_KEY from environment variable

class Production(Config):
    """
    Production configuration class.
    """
    LOGGER = True

class Development(Config):
    """
    Development configuration class.
    """
    LOGGER = True