from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from modelos.clientes import Cliente, ClienteCreate
from database.conexion import get_session

router = APIRouter()


@router.get("/clientes")
def listar_clientes(session: Session = Depends(get_session)):
    return session.exec(select(Cliente)).all()


@router.get("/clientes/{id}")
def buscar_cliente(id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    return cliente


@router.post("/clientes")
def crear_cliente(
    cliente: ClienteCreate,
    session: Session = Depends(get_session)
):
    nuevo_cliente = Cliente.model_validate(cliente)

    session.add(nuevo_cliente)
    session.commit()
    session.refresh(nuevo_cliente)

    return nuevo_cliente


@router.put("/clientes/{id}")
def actualizar_cliente(
    id: int,
    datos: ClienteCreate,
    session: Session = Depends(get_session)
):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    cliente.nombre = datos.nombre
    cliente.correo = datos.correo
    cliente.telefono = datos.telefono

    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    return cliente


@router.delete("/clientes/{id}")
def eliminar_cliente(id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    session.delete(cliente)
    session.commit()

    return {"mensaje": "Cliente eliminado correctamente"}