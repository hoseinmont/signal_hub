from pydantic import BaseModel


class WebhookIncoming(BaseModel):
    message: str
    token: str
