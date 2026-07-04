from typing import Optional
from sqlmodel import SQLModel, Field


class TransaccionBase(SQLModel):
    vr_unitario: float
    cantidad: int
    factura_id: int


class Transaccion(TransaccionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TransaccionCreate(TransaccionBase):
    pass