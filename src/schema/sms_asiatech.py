from pydantic import BaseModel


class SmsAsiatechOutComingSchema(BaseModel):
    message: str
    sender_number: str
    api_key: str
    to_number: str

