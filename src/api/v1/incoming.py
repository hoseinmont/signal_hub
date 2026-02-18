from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from schema import AlertmanagerIncoming, WebhookIncoming, GrafanaOncallInComingSchema
from service import Converter
from config import settings
from utils import logger

router = APIRouter()


@router.post("/alertmanager")
async def alertmanager(
    request: Request,
    alertmanager_incoming: AlertmanagerIncoming,
):
    token: str = request.query_params.get('token')

    out_coming_config = settings.get_out_coming_config('alertmanager', token)

    converter_class = Converter(out_coming_config, alertmanager_incoming)
    function_name = f"from_alertmanager_to_{out_coming_config['to']}"

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


@router.post("/webhook")
async def webhook(
    request: Request,
    webhookIncoming: WebhookIncoming,
):
    out_coming_config = settings.get_out_coming_config('webhook', webhookIncoming.token)

    converter_class = Converter(out_coming_config, webhookIncoming)
    function_name = f"from_webhook_to_{out_coming_config['to']}"

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

@router.post("/grafana-oncall")
async def grafana_oncall(
    request: Request,
    schema: GrafanaOncallInComingSchema,
):
    token: str = request.query_params.get('token')

    out_coming_config = settings.get_out_coming_config('grafana-oncall', token)

    converter_class = Converter(out_coming_config, schema)
    function_name = f"from_grafana_oncall_to_{out_coming_config['to']}"

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


@router.post("/stdout")
async def stdout(
    request: Request,
):
    body = await request.json()
    print(body)
    logger.info(body)

    return JSONResponse(
        status_code=200,
        content={
            "error": False,
            "message": "Successful",
            "data": None
        }
    )


