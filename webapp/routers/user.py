from fastapi import APIRouter, HTTPException, Body
from repositories.user import db_get_text_value, db_upsert_text_value, db_delete_user, db_get_users 

router = APIRouter()

@router.get("/")
def get_user_value(email: str) -> str:    
    val = db_get_text_value(email)    
    if val is None:
        return HTTPException(404, detail=f"User {email} does not exist")
    
    return val[0]

@router.post("/")
def upsert_value(email: str, value: str = Body(...)):    
    db_upsert_text_value(email, value)
    return f"User {email} has been inserted or updated"

@router.delete("/")
def delete_user(email: str):
    db_delete_user(email)
    return f"User {email} has been deleted"

@router.get("/users")
def get_users(limit: int = 10, offset: int = 0):
    users = db_get_users(limit, offset)
    ul = []
    for user in users:
        ul.append({"email": user[0], "text" : user[1]})

    return ul
