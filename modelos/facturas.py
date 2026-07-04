<<<<<<< HEAD

from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class FacturaBase(SQLModel):
    fecha: str
    valor_total: float
=======
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class FacturaBase(SQLModel):
    fecha: str
    valor_total: float
    cliente_id: int = Field(foreign_key="cliente.id")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c


class Factura(FacturaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
<<<<<<< HEAD
    cliente_id: int = Field(foreign_key="cliente.id")
=======
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c

    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: List["Transaccion"] = Relationship(back_populates="factura")


class FacturaCreate(FacturaBase):
<<<<<<< HEAD
    cliente_id: int
=======
    pass
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
