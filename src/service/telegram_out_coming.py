from .outcoming_structure import OutComingStructure
from schema import TelegramOutComingSchema
import requests


class TelegramOutComing(OutComingStructure):

    def send(self, alert: TelegramOutComingSchema):
        url = (f"https://api.telegram.org/bot{alert.token}/sendMessage")
        payload = {
            "text": alert.message,
            "chat_id": alert.chat_id
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Mont",
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)

