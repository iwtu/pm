from fastapi import APIRouter, Form, HTTPException
import orjson
import xml.etree.ElementTree as ET

from utils.transform import transform_json2xml, transform_xml2dict


router = APIRouter()

@router.post("/json2xml")
async def json2xml(jsontext: str = Form(...)):
    jsondict = {}
    try:
        jsondict = orjson.loads(jsontext)
    except:
        raise HTTPException(422, detail="Input is not valid JSON string.")

    return transform_json2xml(jsondict)

@router.post("/xml2json")    
async def xml2json(xmltext: str = Form(...)):
    
    xmlroot = None
    try:         
        xmlroot = ET.fromstring(xmltext)
    except:
        raise HTTPException(422, detail="Input is not valid XML string.")

    return transform_xml2dict(xmlroot)