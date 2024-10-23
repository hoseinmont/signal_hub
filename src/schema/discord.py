from pydantic import BaseModel


class DiscordOutComingSchema(BaseModel):
    message: str
    token: str
    webhook_id: str
