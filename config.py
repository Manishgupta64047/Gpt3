from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 25843661))
API_HASH = getenv("API_HASH", "5e5bdce7ff26e46d224d62298850dec8")
BOT_TOKEN = getenv("BOT_TOKEN", "6031256905:AAG8KoldgPCnzE2yLlalek3xJGohew1kgEs")
OPENAI_API = getenv("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", "") # get api key : https://platform.openai.com/account/api-keys
