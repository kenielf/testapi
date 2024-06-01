import asyncio
from pathlib import Path

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from directories import BASE_DIR
from system import *


router = APIRouter()
templates = Jinja2Templates(BASE_DIR / "templates")

# Static information
kernel = get_kernel()


# Add test routes
@router.get("/api/v1/status", response_class=JSONResponse)
async def status():
    return JSONResponse(
        {
            "status": "active",
            "kernel": kernel,
            "uptime": get_uptime(),
            "cpu_usage": f"{get_cpu_usage():.2f}%",
            "memory_usage": f"{get_memory_usage():.2f}%",
        }
    )


@router.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse("<h1>Hello, world!</h1>")


@router.get("/status", response_class=HTMLResponse)
async def status_page(request: Request):
    return templates.TemplateResponse("status.html", context={"request": request})


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(1)
        await websocket.send_json(
            data={
                "status": "active",
                "kernel": kernel,
                "uptime": get_uptime(),
                "cpu_usage": f"{get_cpu_usage():.2f}%",
                "memory_usage": f"{get_memory_usage():.2f}%",
            }
        )
