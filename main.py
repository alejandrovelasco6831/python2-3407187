from fastapi import FastAPI
from modelos.clientes import Cliente
from modelos.facturas import Factura
from modelos.transacciones import Transaccion

app = FastAPI()

# Listas temporales
clientes = []
facturas = []
transacciones = []

# ==========================
# RUTA PRINCIPAL
# ==========================

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

# ==========================
# CLIENTES
# ==========================

@app.get("/clientes")
def listar_clientes():
    return clientes


@app.get("/clientes/{id}")
def listar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}


@app.post("/clientes")
def crear_cliente(cliente: Cliente):

    clientes.append(cliente)

    return {
        "mensaje": "Cliente agregado",
        "datos": cliente
    }


@app.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            clientes[i] = cliente

            return {
                "mensaje": "Cliente actualizado",
                "datos": cliente
            }

    return {"mensaje": "Cliente no encontrado"}


@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            eliminado = clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado",
                "datos": eliminado
            }

    return {"mensaje": "Cliente no encontrado"}


# ==========================
# FACTURAS
# ==========================

@app.get("/facturas")
def listar_facturas():
    return facturas


@app.post("/facturas")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura agregada",
        "datos": factura
    }


@app.put("/facturas/{id}")
def actualizar_factura(id: int, factura: Factura):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            facturas[i] = factura

            return {
                "mensaje": "Factura actualizada",
                "datos": factura
            }

    return {"mensaje": "Factura no encontrada"}


@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            eliminada = facturas.pop(i)

            return {
                "mensaje": "Factura eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Factura no encontrada"}


# ==========================
# TRANSACCIONES
# ==========================

@app.get("/transacciones")
def listar_transacciones():
    return transacciones


@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción agregada",
        "datos": transaccion
    }


@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion: Transaccion):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            transacciones[i] = transaccion

            return {
                "mensaje": "Transacción actualizada",
                "datos": transaccion
            }

    return {"mensaje": "Transacción no encontrada"}


@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            eliminada = transacciones.pop(i)

            return {
                "mensaje": "Transacción eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Transacción no encontrada"}