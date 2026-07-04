from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from modelos.facturas import Factura, FacturaCreate
from database.conexion import get_session

router = APIRouter()


@router.get("/facturas")
def listar_facturas(session: Session = Depends(get_session)):
    return session.exec(select(Factura)).all()


@router.post("/facturas")
def crear_factura(
    factura: FacturaCreate,
    session: Session = Depends(get_session)
):
    nueva_factura = Factura.model_validate(factura)

    session.add(nueva_factura)
    session.commit()
    session.refresh(nueva_factura)

    return nueva_factura


@router.get("/facturas/{id}")
def buscar_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    return factura


@router.put("/facturas/{id}")
def actualizar_factura(
    id: int,
    datos: FacturaCreate,
    session: Session = Depends(get_session)
):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    factura.fecha = datos.fecha
    factura.valor_total = datos.valor_total
    factura.cliente_id = datos.cliente_id

    session.add(factura)
    session.commit()
    session.refresh(factura)

    return factura


@router.delete("/facturas/{id}")
def eliminar_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    session.delete(factura)
    session.commit()

    return {"mensaje": "Factura eliminada correctamente"}