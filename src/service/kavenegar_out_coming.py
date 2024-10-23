from .outcoming_structure import OutComingStructure
from schema import KavenegarOutComingSchema
import requests
import urllib.parse


class KavenegarOutComing(OutComingStructure):
    token: str = "111"
    sender: str = "111"

    def send(self, alert: KavenegarOutComingSchema):
        url = (f"https://api.kavenegar.com/v1/{self.token}/sms/send.json"
               f"?sender={self.sender}&receptor={alert.receptor}&message={urllib.parse.quote(alert.message)}")
        print(url)
        response = requests.get(url)
        print(response.status_code)
        print(response.json())
