from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from schema import AlertmanagerIncoming, WebhookIncoming, GrafanaOncallInComingSchema
from service import Converter
from config import settings
from utils import logger

router = APIRouter()


@router.post("/grafana-oncall")
async def grafana_oncall(
    request: Request,
    data: GrafanaOncallInComingSchema,
):
    token: str = request.query_params.get('token')
    to: str = request.query_params.get('to')
    value: str = request.query_params.get('value')

    out_coming_config = settings.get_out_coming_config_v2(token, to)
    out_coming_config['value'] = value

    converter_class = Converter(out_coming_config, data)
    function_name = f"from_grafana_oncall_to_{to}"

    # run function ------
    func = getattr(converter_class, function_name)
    result = func()

    return JSONResponse(
        status_code=200,
        content={
            "error": False,
            "message": "Successful",
            "data": None
        }
    )
