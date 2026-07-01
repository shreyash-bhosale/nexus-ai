"""
Application settings.
"""

import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "NEXUS AI"
VERSION = "0.1.0"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")