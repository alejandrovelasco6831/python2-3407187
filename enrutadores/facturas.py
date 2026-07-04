from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from modelos.facturas import Factura, FacturaCreate
<<<<<<< HEAD
from modelos.clientes import Cliente
from database.conexion import get_session

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)


@router.get("/")
def listar_facturas(session: Session = Depends(get_session)):
    facturas = session.exec(select(Factura)).all()

    resultado = []

    for factura in facturas:
        cliente = session.get(Cliente, factura.cliente_id)

        resultado.append({
            "id": factura.id,
            "fecha": factura.fecha,
            "valor_total": factura.valor_total,
            "cliente": cliente
        })

    return resultado


@router.post("/")
=======
from database.conexion import get_session

router = APIRouter()


@router.get("/facturas")
def listar_facturas(session: Session = Depends(get_session)):
    return session.exec(select(Factura)).all()


@router.post("/facturas")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def crear_factura(
    factura: FacturaCreate,
    session: Session = Depends(get_session)
):
    nueva_factura = Factura.model_validate(factura)

    session.add(nueva_factura)
    session.commit()
    session.refresh(nueva_factura)

    return nueva_factura


<<<<<<< HEAD
@router.get("/{id}")
=======
@router.get("/facturas/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def buscar_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

<<<<<<< HEAD
    cliente = session.get(Cliente, factura.cliente_id)

    return {
        "id": factura.id,
        "fecha": factura.fecha,
        "valor_total": factura.valor_total,
        "cliente": cliente
    }


@router.put("/{id}")
=======
    return factura


@router.put("/facturas/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
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


<<<<<<< HEAD
@router.delete("/{id}")
=======
@router.delete("/facturas/{id}")
>>>>>>> 586134f5fc7db877d11fdf004ad14c0c3ebeb55c
def eliminar_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    session.delete(factura)
    session.commit()

    return {"mensaje": "Factura eliminada correctamente"}