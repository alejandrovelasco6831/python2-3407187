
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class ClienteBase(SQLModel):
    nombre: str
    correo: str
    telefono: str


class Cliente(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    facturas: List["Factura"] = Relationship(back_populates="cliente")


class ClienteCreate(ClienteBase):
    pass


class ClienteRead(ClienteBase):
    id: int


class ClienteReadConFacturas(ClienteRead):
    facturas: list = []