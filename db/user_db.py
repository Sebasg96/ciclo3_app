from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username:str
    nombres: str
    apellidos: str
    password:str
    fecha_registro: str
    activo = bool
    
db_users = Dict[str, UserInDB]

def get_user(username: str):
    if username in db_users.keys():
        return db_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    db_users[user_in_db.username] = user_in_db
    return user_in_db

def create_user(new_user: UserInDB):
    db_users[new_user.username] = {UserInDB.nombres, UserInDB.apellidos, UserInDB.password, UserInDB.fecha_registro, UserInDB.activo}