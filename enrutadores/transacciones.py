from fastapi import APIRouter
from modelos.transacciones import Transaccion

router = APIRouter()

transacciones = []

@router.get("/transacciones")
def listar_transacciones():
    return transacciones


@router.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción agregada",
        "datos": transaccion
    }


@router.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion: Transaccion):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            transacciones[i] = transaccion

            return {
                "mensaje": "Transacción actualizada",
                "datos": transaccion
            }

    return {"mensaje": "Transacción no encontrada"}


@router.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            eliminada = transacciones.pop(i)

            return {
                "mensaje": "Transacción eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Transacción no encontrada"}