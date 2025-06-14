from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
	TOKEN = os.getenv("BOT_TOKEN")

settings = Settings()