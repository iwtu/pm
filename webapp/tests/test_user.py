from fastapi.testclient import TestClient
from unittest import mock

from main import app

client = TestClient(app)


# def test_get_user_value():
#     expected_text = "Power Medical is AWESOME!!!"
#     query_result = (expected_text, )
#     with mock.patch('psycopg2.connect') as mock_connect:
#         mock_con_cm = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
#         mock_con = mock_con_cm.__enter__.return_value  # object assigned to con in with ... as con 
#         mock_cur = mock_con.cursor.return_value  # result of con.cursor(cursor_factory=DictCursor)
#         mock_cur.fetchone.return_value = query_result  # return this when calling cur.fetchall()

#         resp = client.get("/api/user?email=adrian@pm.com")

#         print(resp.text)
#         assert resp.status_code == 200
#         assert resp.text == expected_text