from typing import Optional

from pydantic import BaseModel
from .alertmanager import AlertmanagerIncoming

class GrafanaOncallInComingSchema(BaseModel):
    alert_payload: Optional[AlertmanagerIncoming]
