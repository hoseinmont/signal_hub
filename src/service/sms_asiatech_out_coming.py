from .outcoming_structure import OutComingStructure
from schema import SmsAsiatechOutComingSchema
import requests


class SmsAsiatechOutComing(OutComingStructure):

    def send(self, item: SmsAsiatechOutComingSchema):
        url = f"https://smsapi.asiatech.ir/api/1/message/send"

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "X-API-Key": item.api_key,
            "scope": "ApiAccess"
        }

        body = [{
            "SourceAddress": item.sender_number,
            "MessageText": item.message,
            "DestinationAddress": item.to_number,
        }]
        try:
            req = requests.post(url, headers=headers, json=body)
            # print(req.content.decode("utf-8"))
        except Exception as e:
            print(e)
