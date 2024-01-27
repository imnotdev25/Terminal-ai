from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = getenv("API_KEY")