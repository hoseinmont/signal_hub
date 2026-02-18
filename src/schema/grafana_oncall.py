from pydantic import BaseModel


class GrafanaOncallInComingSchema(BaseModel):
    message: str
    token: str
    chat_id: str
