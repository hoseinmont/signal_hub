from typing import Optional

from pydantic import BaseModel
from .alertmanager import AlertmanagerIncoming


class Permalinks(BaseModel):
    web: Optional[str] = None


class AlertGroup(BaseModel):
    permalinks: Optional[Permalinks]


class GrafanaOncallInComingSchema(BaseModel):
    alert_payload: Optional[AlertmanagerIncoming]
    alert_group: Optional[AlertGroup]