from telethon import events
from KiritoRobot import telethn
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register(**args):
    """
    Register a new message event handler.
    """
    pattern = args.get("pattern", None)

    # Ensure the pattern starts with a command prefix
    r_pattern = r"^[/!]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        telethn.add_event_handler(func, events.NewMessage(**args))
        logger.info(f"Registered message handler for pattern: {pattern}")
        return func

    return decorator

def chataction(**args):
    """
    Register a chat action event handler.
    """
    def decorator(func):
        telethn.add_event_handler(func, events.ChatAction(**args))
        logger.info("Registered chat action handler.")
        return func

    return decorator

def userupdate(**args):
    """
    Register a user update event handler.
    """
    def decorator(func):
        telethn.add_event_handler(func, events.UserUpdate(**args))
        logger.info("Registered user update handler.")
        return func

    return decorator

def inlinequery(**args):
    """
    Register an inline query event handler.
    """
    pattern = args.get("pattern", None)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    def decorator(func):
        telethn.add_event_handler(func, events.InlineQuery(**args))
        logger.info(f"Registered inline query handler for pattern: {pattern}")
        return func

    return decorator

def callbackquery(**args):
    """
    Register a callback query event handler.
    """
    def decorator(func):
        telethn.add_event_handler(func, events.CallbackQuery(**args))
        logger.info("Registered callback query handler.")
        return func

    return decorator