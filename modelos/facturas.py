from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class FacturaBase(SQLModel):
    fecha: str
    valor_total: float
    cliente_id: int = Field(foreign_key="cliente.id")


class Factura(FacturaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: List["Transaccion"] = Relationship(back_populates="factura")


class FacturaCreate(FacturaBase):
    pass