from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from modelos.transacciones import Transaccion, TransaccionCreate
from database.conexion import get_session

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


@router.get("/transacciones")
def listar_transacciones(session: Session = Depends(get_session)):
    return session.exec(select(Transaccion)).all()


@router.post("/transacciones")
def crear_transaccion(
    transaccion: TransaccionCreate,
    session: Session = Depends(get_session)
):
    nueva_transaccion = Transaccion.model_validate(transaccion)

    session.add(nueva_transaccion)
    session.commit()
    session.refresh(nueva_transaccion)

    return nueva_transaccion


@router.get("/transacciones/{id}")
def buscar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    return transaccion


@router.put("/transacciones/{id}")
def actualizar_transaccion(
    id: int,
    datos: TransaccionCreate,
    session: Session = Depends(get_session)
):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    transaccion.vr_unitario = datos.vr_unitario
    transaccion.cantidad = datos.cantidad
    transaccion.factura_id = datos.factura_id

    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)

    return transaccion


@router.delete("/transacciones/{id}")
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    session.delete(transaccion)
    session.commit()

    return {"mensaje": "Transacción eliminada correctamente"}