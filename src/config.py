# config.py

import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()


def get_oauth_token():
    """
    Retrieves the SoundCloud OAuth token from environment variables.
    """
    token = os.getenv('SOUNDCLOUD_OAUTH_TOKEN')
    if not token:
        raise ValueError("OAuth token not found. Please set SOUNDCLOUD_OAUTH_TOKEN in your .env file.")
    return token

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
