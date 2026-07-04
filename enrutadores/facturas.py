from fastapi import APIRouter
from modelos.facturas import Factura

router = APIRouter()

facturas = []

@router.get("/facturas")
def listar_facturas():
    return facturas


@router.post("/facturas")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura agregada",
        "datos": factura
    }


@router.put("/facturas/{id}")
def actualizar_factura(id: int, factura: Factura):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            facturas[i] = factura

            return {
                "mensaje": "Factura actualizada",
                "datos": factura
            }

    return {"mensaje": "Factura no encontrada"}


@router.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            eliminada = facturas.pop(i)

            return {
                "mensaje": "Factura eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Factura no encontrada"}