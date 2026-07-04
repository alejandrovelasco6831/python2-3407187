from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class TransaccionBase(SQLModel):
    vr_unitario: float
    cantidad: int
    factura_id: int = Field(foreign_key="factura.id")


class Transaccion(TransaccionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
<<<<<<< HEAD
    factura_id: int = Field(foreign_key="factura.id")
=======
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c

    factura: Optional["Factura"] = Relationship(back_populates="transacciones")


class TransaccionCreate(TransaccionBase):
<<<<<<< HEAD
    pass


"""
CREATE TABLE transaccion (
        vr_unitario FLOAT NOT NULL, 
        cantidad INTEGER NOT NULL, 
        factura_id INTEGER NOT NULL, 
        id INTEGER NOT NULL, 
        PRIMARY KEY (id)
        FOREIGN KEY(factura_id) REFERENCES factura(id)
);
"""
=======
    pass
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
