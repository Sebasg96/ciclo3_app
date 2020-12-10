from db.user_db import UserInDB
from db.user_db import create_user, get_user
from models.user_models import UserOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

#Consultar usuario
@api.get("/user/{username}")
async def get_user_information(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe.")
    if user_in_db.active == False:
        return {"message": "El usuario ya no se encuentra activo."}
    user_out = UserOut(**user_in_db.dict())
    return user_out

#Crear usuario
@api.put("/user/create")
async def add_user(user: UserInDB):
    create_user(user)
    user_out = UserOut(**user.dict())
    return user_out

#Dar de baja un usuario
@api.put("/user/delete")
async def unsubscribe_user(username: str):
    user_in_db = get_user(username)
    user_in_db.active = False
    return {"message": "El usuario ha sido dado de baja."}
