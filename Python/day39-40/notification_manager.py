import requests
from datetime import datetime, timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

#the path for the ENV
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)
API_KEY = os.getenv('API_Telegram_KEY')
ID = os.getenv("CHAT_ID")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.token = API_KEY
        self.id = ID

    def sendtext(self, bot_message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        params = {
            "chat_id": self.id,
            "text": bot_message,
        }
        response = requests.post(
            url,
            json=params,
            timeout=15
        )
        print("Telegram status:", response.status_code)
        print("Telegram response:", response.json()['ok'])
        response.raise_for_status()