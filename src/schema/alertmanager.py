from pydantic import BaseModel
from typing import List, Optional


class Label(BaseModel):
    alertname: Optional[str] = None
    severity: Optional[str] = None


class Annotation(BaseModel):
    description: Optional[str] = None
    summary: Optional[str] = None


class Alert(BaseModel):
    status: str
    labels: Optional[Label]
    annotations: Optional[Annotation]


class AlertmanagerIncoming(BaseModel):
    alerts: List[Alert]
