from pydantic import BaseModel


class KavenegarOutComingSchema(BaseModel):
    message: str
    receptor: str
