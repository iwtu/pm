from fastapi.testclient import TestClient
import xml.etree.ElementTree as ET

from main import app



client = TestClient(app)

def test_transform_json2xml():
    jsontext = '{"apple":7,"orange":4.1,"other":{"banana":"fruit"},"many":[true,"thing",{"pineapple":null}]}'
    resp = client.post("/transform/json2xml", data={"jsontext": jsontext})

    assert resp.status_code == 200
    #print(resp.text)
    #ET.fromstring(resp.text)

def test_transform_xml2json():
        xmltext = '<ITEM type="object"><ITEM key="apple" type="integer" value="7"/></ITEM>'
        resp = client.post("/transform/xml2json", data={"xmltext": xmltext})

        assert resp.status_code == 200