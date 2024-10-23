from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from schema import AlertmanagerIncoming, WebhookIncoming
from service import Converter
from config import settings


router = APIRouter()


@router.post("/alertmanager")
async def alertmanager(
    request: Request,
    alertmanagerIncoming: AlertmanagerIncoming,
):
    out_coming_config = settings.get_out_coming_config('alertmanager', alertmanagerIncoming.token)

    converter_class = Converter(out_coming_config, alertmanagerIncoming)
    function_name = f"from_alertmanager_to_{out_coming_config['to']}"

    # run function ------
    func = getattr(converter_class, function_name)
    result = func()

    return JSONResponse(
        status_code=200,
        content={
            "error": True,
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
            "error": True,
            "message": "Successful",
            "data": None
        }
    )
