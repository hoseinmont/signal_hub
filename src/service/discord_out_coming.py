from .outcoming_structure import OutComingStructure
from schema import DiscordOutComingSchema
import requests


class DiscordOutComing(OutComingStructure):

    def send(self, alert: DiscordOutComingSchema):
        url = (f"https://discord.com/api/webhooks/{alert.webhook_id}/{alert.token}")
        payload = {
            "content": alert.message,
            "username": "oooooOOOoooo",
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Mont",
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)

