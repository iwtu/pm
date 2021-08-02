from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from routers.transform import router as transform_router

app = FastAPI()

app.include_router(
    transform_router,
    prefix="/transform",
    tags=["json2xml", "xml2json"]
)

@app.get("/")
async def index(request: Request):
    return FileResponse("static/index.html")

