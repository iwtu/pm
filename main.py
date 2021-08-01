from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import FileResponse
import orjson

from utils import transform_json2xml

app = FastAPI()

@app.get("/")
async def index(request: Request):
    return FileResponse("static/index.html")


@app.post("/json2xml")
async def json2xml(jsontext: str = Form(...)):
    jsondict = {}
    try:
        jsondict = orjson.loads(jsontext)
    except:
        raise HTTPException(422, detail="Input is not valid JSON string.")

    return transform_json2xml(jsondict)


@app.post("/xml2json")    
async def xml2json(xmltext: str = Form(...)):
    return xmltext