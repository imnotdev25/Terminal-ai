import os.path
from os import getenv

from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~") + "/.env")

API_KEY = getenv("API_KEY")
