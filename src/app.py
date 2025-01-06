import logging
from config import settings
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse

from starlette.middleware.cors import CORSMiddleware

from exception import NotFoundException, UnauthorizedException

from api.v1.incoming import router as incoming

if not settings.DEBUG:
    import sentry_sdk
    sentry_sdk.init(settings.SENTRY_DSN)


logging.basicConfig(level=settings.LOG_LEVEL)
logging.info(f"[{settings.APP_TITLE} STARTED]")


app = FastAPI(title=settings.APP_TITLE)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

routerV1 = APIRouter()
routerV1.include_router(incoming)

app.include_router(routerV1, prefix='/v1')


routerMain = APIRouter()

@routerMain.get("/ping")
async def ping():
    return JSONResponse(status_code=200, content={"error": False, "message": "OK"})

app.include_router(routerMain)


@app.exception_handler(NotFoundException)
async def notfound_handler(request: Request, e: NotFoundException):
    return JSONResponse(status_code=e.status, content={"error": True, "message": e.message, "data": None})


@app.exception_handler(UnauthorizedException)
async def notfound_handler(request: Request, e: UnauthorizedException):
    return JSONResponse(status_code=e.status, content={"error": True, "message": e.message, "data": None})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
