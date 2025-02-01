import asyncio
import sys
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from KiritoRobot import MONGO_DB_URI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB configuration
MONGO_DB = "KiritoRobot"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_DB_URI)
db = client[MONGO_DB]

async def test_connection():
    """
    Test the MongoDB connection.
    """
    try:
        await client.server_info()
        logger.info("Connected to MongoDB successfully!")
    except ServerSelectionTimeoutError:
        logger.critical("Failed to connect to MongoDB. Exiting...")
        sys.exit(1)

# Test the connection on startup
asyncio.get_event_loop().run_until_complete(test_connection())