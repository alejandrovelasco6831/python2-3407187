from fastapi import APIRouter
from modelos.clientes import Cliente

router = APIRouter()

clientes = []

@router.get("/clientes")
def listar_clientes():
    return clientes


@router.get("/clientes/{id}")
def listar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}


@router.post("/clientes")
def crear_cliente(cliente: Cliente):

    clientes.append(cliente)

    return {
        "mensaje": "Cliente agregado",
        "datos": cliente
    }


@router.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            clientes[i] = cliente

            return {
                "mensaje": "Cliente actualizado",
                "datos": cliente
            }

    return {"mensaje": "Cliente no encontrado"}


@router.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            eliminado = clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado",
                "datos": eliminado
            }

    return {"mensaje": "Cliente no encontrado"}