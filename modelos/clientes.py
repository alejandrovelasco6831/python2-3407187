from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str