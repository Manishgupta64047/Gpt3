from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 17954446))
API_HASH = getenv("API_HASH", "b9d62d60af7542ad41274a47a5c9f369")
BOT_TOKEN = getenv("BOT_TOKEN", "6076583524:AAGSxIip3IgBytYq3i0jjIEDbVRMD3FFcno")
OPENAI_API = getenv("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", "") # get api key : https://platform.openai.com/account/api-keys
