from typing import Dict
from pydantic import BaseModel
from datetime import date
from datetime import datetime

class UserInDB(BaseModel):
    username:str
    nombres: str
    apellidos: str
    email: str
    password:str
    active = bool
    fecha_registro: str
    
    
db_users = Dict[str, UserInDB]

db_users = {
    "carlitosmota": UserInDB(**{"username":"carlitosmota",
                                "nombres":"Carlos",
                                "apellidos":"Perez Mota",
                                "email":"capeta01@gmail.com",
                                "password":"123456",
                                "active":True,
                                "fecha_registro":"2012-05-01 05:34:01"}),

    "nando_duca": UserInDB(**{"username":"nando_duca",
                              "nombres":"Fernando",
                              "apellidos":"Duarte Camacho",
                              "email":"feducho2@gmail.com",
                              "password":"234567",
                              "active":True,
                              "fecha_registro":"2012-04-30 10:14:23"}),

    "maricami": UserInDB(**{"username":"maricami",
                            "nombres":"Maria camila",
                            "apellidos":"Estrada Tobon",
                            "email":"mariestrada@hotmail.com",
                            "password":"987654",
                            "active":False,
                            "fecha_registro":"2011-10-01 05:34:01"}),

    "crimar": UserInDB(**{"username":"crimar",
                                "nombres":"Cristina",
                                "apellidos":"Martinez Ortiz",
                                "email":"crimar01@hotmail.com",
                                "password":"5566214",
                                "active":False,
                                "fecha_registro":"2009-08-22 05:41:12"}),

    "meligar": UserInDB(**{"username":"meligar",
                              "nombres":"Melissa",
                              "apellidos":"Garcia Gomez",
                              "email":"meligar80@gmail.com",
                              "password":"965621",
                              "active":True,
                              "fecha_registro":"2011-11-30 04:51:20"}),

    "nata": UserInDB(**{"username":"nata",
                            "nombres":"Natalia Andrea",
                            "apellidos":"Pino",
                            "email":"pinonata@hotmail.com",
                            "password":"124515",
                            "active":True,
                            "fecha_registro":"2014-08-20 09:14:41"}),                                                    
}

def get_user(username: str):
    if username in db_users.keys():
        return db_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    db_users[user_in_db.username] = user_in_db
    return user_in_db

def create_user(new_user: UserInDB):
    db_users[new_user.username] = {UserInDB.nombres, UserInDB.apellidos, UserInDB.email, UserInDB.password, UserInDB.active, UserInDB.fecha_registro}
