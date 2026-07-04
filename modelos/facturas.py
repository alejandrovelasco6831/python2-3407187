from typing import Optional
from sqlmodel import SQLModel, Field


class FacturaBase(SQLModel):
    fecha: str
    valor_total: float
    cliente_id: int


class Factura(FacturaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class FacturaCreate(FacturaBase):
    pass