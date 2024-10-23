from pydantic import BaseModel


class TelegramOutComingSchema(BaseModel):
    message: str
    token: str
    chat_id: str
