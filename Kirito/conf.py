import os
import sys
import logging as log
from envparse import env

# Set up logging
log.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=log.INFO,
)

LOGGER = log.getLogger(__name__)

# Default values for configuration keys
DEFAULTS = {
    "LOAD_MODULES": True,
}

def get_str_key(name, required=False):
    """
    Get a string value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.str(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_int_key(name, required=False):
    """
    Get an integer value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.int(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_bool_key(name, required=False):
    """
    Get a boolean value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.bool(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_list_key(name, required=False):
    """
    Get a list value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.list(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_dict_key(name, required=False):
    """
    Get a dictionary value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.dict(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_float_key(name, required=False):
    """
    Get a float value from environment variables.
    If the key is not found and is not required, return None.
    If the key is required but not found, exit the program.
    """
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None

    data = env.float(name, default=default)

    if not data and required:
        LOGGER.critical(f"Required environment variable '{name}' is missing!")
        sys.exit(2)
    elif not data:
        LOGGER.warning(f"Optional environment variable '{name}' is missing.")
        return None
    else:
        return data

def get_env_vars():
    """
    Load all environment variables from a .env file if it exists.
    """
    env_file = os.path.join(os.getcwd(), ".env")
    if os.path.exists(env_file):
        env.read_envfile(env_file)
        LOGGER.info(f"Loaded environment variables from {env_file}")
    else:
        LOGGER.warning("No .env file found. Using environment variables from the system.")

# Load environment variables
get_env_vars()