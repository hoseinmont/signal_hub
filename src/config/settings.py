from pydantic import BaseModel
from typing import Dict
from exception import NotFoundException


class Settings(BaseModel):

    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    SENTRY_DSN: str = ""
    APP_TITLE: str = "from-star-to-star"

    ITO: Dict = {
        "token1": {
            "alertmanager": {
                "to": "telegram",
                "telegram_token": "1234",
                "chat_id": "1234",
            },
            "webhook": {
                "to": "telegram",
                "telegram_token": "1234",
                "chat_id": "1234",
            }
        },
        "token2": {
            "alertmanager": {
                "to": "telegram",
                "telegram_token": "1234",
                "chat_id": "1234",
            },
            "webhook": {
                "to": "discord",
                "webhook_token": "1234",
                "webhook_id": "1234",
            }
        }
    }

    class Config:
        case_sensitive = True

    def get_out_coming_config(self, incoming: str, token: str):
        if token in self.ITO and incoming in self.ITO[token]:
            return self.ITO[token][incoming]
        else:
            raise NotFoundException("Out coming config not found.")


settings = Settings()

