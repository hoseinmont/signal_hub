from .outcoming_structure import OutComingStructure
from schema import TelegramOutComingSchema
import requests
from fastapi.responses import JSONResponse


class TelegramOutComing(OutComingStructure):

    def send(self, alert: TelegramOutComingSchema):
        url = (f"https://api.telegram.org/bot{alert.token}/sendMessage")
        payload = {
            "text": alert.message,
            "chat_id": alert.chat_id
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "basalam-alert",
            "content-type": "application/json"
        }
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return JSONResponse(
                status_code=500,
                content={
                    "error": True,
                    "message": "Telegram Timeout",
                    "data": None
                }
            )

