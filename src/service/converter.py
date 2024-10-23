from .telegram_out_coming import TelegramOutComing
from .discord_out_coming import DiscordOutComing
from schema import TelegramOutComingSchema, DiscordOutComingSchema
from typing import Dict


class Converter:
    out_coming_config: Dict
    data: Dict

    def __init__(self, out_coming_config, data):
        self.out_coming_config = out_coming_config
        self.data = data

    def from_alertmanager_to_telegram(self):
        for alert in self.data.alerts:
            message = f"""
status: {alert.status}
alertname: {alert.labels.alertname}
severity: {alert.labels.severity}
description: {alert.annotations.description}
"""

            TelegramOutComing().send(TelegramOutComingSchema(
                message=message,
                token=self.out_coming_config['telegram_token'],
                chat_id=self.out_coming_config['chat_id'],
            ))

    def from_webhook_to_telegram(self):
        TelegramOutComing().send(TelegramOutComingSchema(
            message=self.data.message,
            token=self.out_coming_config['telegram_token'],
            chat_id=self.out_coming_config['chat_id'],
        ))

    def from_webhook_to_discord(self):
        DiscordOutComing().send(DiscordOutComingSchema(
            message=self.data.message,
            token=self.out_coming_config['webhook_token'],
            webhook_id=self.out_coming_config['webhook_id'],
        ))
