from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from modelos.transacciones import Transaccion, TransaccionCreate
<<<<<<< HEAD
from modelos.facturas import Factura
from modelos.clientes import Cliente
from database.conexion import get_session

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


@router.get("/")
def listar_transacciones(session: Session = Depends(get_session)):
    transacciones = session.exec(select(Transaccion)).all()

    resultado = []

    for transaccion in transacciones:
        factura = session.get(Factura, transaccion.factura_id)

        cliente = None
        if factura:
            cliente = session.get(Cliente, factura.cliente_id)

        resultado.append({
            "id": transaccion.id,
            "vr_unitario": transaccion.vr_unitario,
            "cantidad": transaccion.cantidad,
            "factura": factura,
            "cliente": cliente
        })

    return resultado


@router.post("/")
=======
from database.conexion import get_session

router = APIRouter()


@router.get("/transacciones")
def listar_transacciones(session: Session = Depends(get_session)):
    return session.exec(select(Transaccion)).all()


@router.post("/transacciones")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def crear_transaccion(
    transaccion: TransaccionCreate,
    session: Session = Depends(get_session)
):
    nueva_transaccion = Transaccion.model_validate(transaccion)

    session.add(nueva_transaccion)
    session.commit()
    session.refresh(nueva_transaccion)

    return nueva_transaccion


<<<<<<< HEAD
@router.get("/{id}")
=======
@router.get("/transacciones/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def buscar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

<<<<<<< HEAD
    factura = session.get(Factura, transaccion.factura_id)

    cliente = None
    if factura:
        cliente = session.get(Cliente, factura.cliente_id)

    return {
        "id": transaccion.id,
        "vr_unitario": transaccion.vr_unitario,
        "cantidad": transaccion.cantidad,
        "factura": factura,
        "cliente": cliente
    }


@router.put("/{id}")
=======
    return transaccion


@router.put("/transacciones/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
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


<<<<<<< HEAD
@router.delete("/{id}")
=======
@router.delete("/transacciones/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    session.delete(transaccion)
    session.commit()

    return {"mensaje": "Transacción eliminada correctamente"}