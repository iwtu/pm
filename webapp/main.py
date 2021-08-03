from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from routers.transform import router as transform_router
from routers.user import router as user_router

app = FastAPI()

app.include_router(
    transform_router,
    prefix="/transform",
    tags=["json2xml", "xml2json"]
)

app.include_router(
    user_router,
    prefix="/api/user",
    tags=["user"]
)

@app.get("/")
async def index(request: Request):
    return FileResponse("static/index.html")

