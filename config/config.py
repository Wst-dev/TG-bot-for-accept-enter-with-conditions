import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Config(BaseModel):
    bot_token: str = os.getenv("BOT_TOKEN")
    channel_id: list[str] = os.getenv("CHANNEL_ID").split(",")
    main_channel_id: str = os.getenv("MAIN_CHANNEL_ID")

config = Config()


