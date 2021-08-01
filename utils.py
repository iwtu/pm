import xml.etree.ElementTree as ET
from typing import Dict
import logging

def transform_json2xml(jsonDict: Dict) -> str:   
    return _transform_json2xml(None, jsonDict)

def _transform_json2xml(key: str, obj: object) -> str:    
    
    t = _get_type(obj)

    if _is_leaf(obj):
        if key is None:
            return f'<ITEM type="{t}" value="{obj}"/>'
        else:
            return f'<ITEM key="{key}" type="{t}" value="{obj}"/>'
    
    if key is None:
        xml = f'<ITEM type="{t}">'
    else:
        xml = f'<ITEM key="{key}" type="{t}">'
    
    if type(obj) == type([]):
        for item in obj:
            xml = xml + _transform_json2xml(None, item)
    
    if type(obj) == type({}):
        for k, v in obj.items():        
            xml = xml + _transform_json2xml(k, v)        

    return xml + '</ITEM>'

def _get_type(obj: object) -> str:
    if type(obj) == type(1):
        return "integer"
    elif type(obj) == type(2.718281828):
        return "float"
    elif type(obj) == type(True):
        return "boolean"    
    elif type(obj) == type("powermedicalisawesome"):
        return "string"
    elif type(obj) == type(None):
        return "null"
    elif type(obj) == type([1]):
        return "list"
    elif (type(obj)) == type({}):
        return "object"    
    else:
        logging.warning(f"Unexpected type {type(obj)} for object {obj}")
        return "uknown"    

def _is_leaf(obj: object) -> bool:
    if type(obj) == type(1):
        return True
    elif type(obj) == type(2.718281828):
        return True
    elif type(obj) == type(True):
        return True
    elif type(obj) == type("powermedicalisawesome"):
        return True
    elif type(obj) == None:
        return True
    else:
        return False

def transform_xml2dict(node: ET.Element) -> Dict:

    key = None
    value = None
    tname = node.attrib["type"].lower()
    if "key" in node.attrib: key = node.attrib["key"]
    if "value" in node.attrib: value = _get_value(tname, node.attrib["value"])

    if value is not None or tname == "null":
        return value

    if tname == "list":
        a = []
        for child in node:
            a.append(transform_xml2dict(child))
        return a

    if tname == "object":
        d = {}        
        for child in node:
            d[child.attrib["key"]] = transform_xml2dict(child)
        return d


def _get_value(typestring: str, valuestring: str):
    ts = typestring.lower()
    if ts == "integer":
        return int(valuestring)
    elif ts == "float":
        return float(valuestring)
    elif ts.startswith("bool"):
        return bool(valuestring)
    elif ts == "string":
        return valuestring
    elif ts == "null" or ts == "none":
        return None
    

