from typing import Optional
from sqlmodel import SQLModel, Field


class ClienteBase(SQLModel):
    nombre: str
    correo: str
    telefono: str


class Cliente(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ClienteCreate(ClienteBase):
    pass