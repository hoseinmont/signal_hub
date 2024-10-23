from pydantic import BaseModel
from typing import List, Optional


class Label(BaseModel):
    alertname: str
    severity: str


class Annotation(BaseModel):
    description: Optional[str]
    summary: Optional[str]


class Alert(BaseModel):
    status: str
    labels: Optional[Label]
    annotations: Optional[Annotation]


class AlertmanagerIncoming(BaseModel):
    alerts: List[Alert]
    token: str
