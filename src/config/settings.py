from pydantic_settings import BaseSettings
from typing import Dict
from exception import NotFoundException
import json
import io


class Settings(BaseSettings):

    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    SENTRY_DSN: str = ""
    APP_TITLE: str = "signal_hub"

    CONFIG_FILE_PATH: str = ""
    CONFIG_FILE_PATH_V2: str = ""

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

    ITO_V2: Dict = {}

    def __init__(self):
        super().__init__()

        if self.CONFIG_FILE_PATH != "":
            with io.open(self.CONFIG_FILE_PATH, 'r', encoding='utf-8') as config_file:
                self.ITO = json.loads(config_file.read())

        if self.CONFIG_FILE_PATH_V2 != "":
            with io.open(self.CONFIG_FILE_PATH_V2, 'r', encoding='utf-8') as config_file:
                self.ITO_V2 = json.loads(config_file.read())


    class Config:
        case_sensitive = True

    def get_out_coming_config(self, incoming: str, token: str):
        if token in self.ITO and incoming in self.ITO[token]:
            return self.ITO[token][incoming]
        else:
            raise NotFoundException("Out Going config not found.")

    def get_out_coming_config_v2(self, token: str, outgoing: str):
        if token in self.ITO_V2 and outgoing in self.ITO[token]:
            return self.ITO_V2[token][outgoing]
        else:
            raise NotFoundException("Out Going config not found.")


settings = Settings()

