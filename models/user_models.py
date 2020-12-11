from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    nombres: str
    apellidos: str
    fecha_registro: str
    correo: str