from config import settings
from database import Database

db = Database(settings)
db.open_connection()

def db_get_text_value(email: str) -> str:
    q = "SELECT value FROM user_values WHERE email = %s"
    v = (email,)
    return db.select_row(q, v) 

def db_upsert_text_value(email:str, val: str) -> int:
    q = "INSERT INTO user_values (email, value) VALUES (%s, %s) ON CONFLICT (email) DO UPDATE SET value = %s "
    v = (email, val, val)
    return db.execute_query(q, v)
    

def db_delete_user(email: str) -> int:
    q = "DELETE FROM user_values WHERE email = %s"
    v = (email,)
    return db.execute_query(q, v)

def db_get_users(limit: int, offset: int):
    q = "SELECT email, value FROM user_values ORDER BY email LIMIT %s OFFSET %s"
    v = (limit, offset)
    return db.select_rows(q, v)
