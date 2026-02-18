from .telegram_out_coming import TelegramOutComing
from .discord_out_coming import DiscordOutComing
from .sms_asiatech_out_coming import SmsAsiatechOutComing
from schema import TelegramOutComingSchema, DiscordOutComingSchema, SmsAsiatechOutComingSchema
from typing import Dict


class Converter:
    out_coming_config: Dict
    data: Dict

    def __init__(self, out_coming_config, data):
        self.out_coming_config = out_coming_config
        self.data = data

    def from_alertmanager_to_telegram(self):
        for alert in self.data.alerts:
            l = '🟢'
            if alert.status == 'firing':
                l = '🔴'

            message = f"""{l}

alertname: {alert.labels.alertname}
status: {alert.status}
severity: {alert.labels.severity}
description: {alert.annotations.description}

{l}
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


    def from_grafana_oncall_to_telegram(self):
        for alert in self.data.alert_payload.alerts:
            l = '🟢'
            if alert.status == 'firing':
                l = '🔴'

            message = f"""{l}

alertname: {alert.labels.alertname}
status: {alert.status}
severity: {alert.labels.severity}
description: {alert.annotations.description}
Link: {self.data.alert_group.permalinks.web}

{l}
"""

            TelegramOutComing().send(TelegramOutComingSchema(
                message=message,
                token=self.out_coming_config['telegram_token'],
                chat_id=self.out_coming_config['chat_id'],
            ))


    def from_grafana_oncall_to_smsapi_asiatech(self):
        for alert in self.data.alert_payload.alerts:
            message = f"Alert {alert.labels.alertname}: {alert.annotations.description}"

            SmsAsiatechOutComing().send(SmsAsiatechOutComingSchema(
                message=message,
                api_key=self.out_coming_config['api_key'],
                sender_number=self.out_coming_config['sender_number'],
                to_number=self.out_coming_config['to_number'],
            ))



