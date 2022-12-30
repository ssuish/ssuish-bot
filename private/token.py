import os
from dotenv import load_dotenv

def get_token() -> str:
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    return token