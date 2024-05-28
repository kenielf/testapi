from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()

# Add test routes
@router.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse("<h1>Hello, world!</h1>")

@router.get("/api/v1/status", response_class=JSONResponse)
async def status():
    return JSONResponse({"status": "active"})
