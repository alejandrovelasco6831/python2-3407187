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
<<<<<<< HEAD
    facturas: list = []  
=======
    facturas: list = []
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
