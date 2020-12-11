from pydantic import BaseModel
from datetime import datetime


class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    nombres: str
    apellidos: str
    fecha_registro: datetime
    email: str