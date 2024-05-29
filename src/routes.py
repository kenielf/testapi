from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from system import *

router = APIRouter()

# Static information
kernel = get_kernel()

# Add test routes
@router.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse("<h1>Hello, world!</h1>")

@router.get("/api/v1/status", response_class=JSONResponse)
async def status():
    return JSONResponse({
        "status": "active",
        "kernel": kernel,
        "uptime": get_uptime(),
        "cpu_usage": f"{get_cpu_usage():.2f}%",
        "memory_usage": f"{get_memory_usage():.2f}%",
    })
