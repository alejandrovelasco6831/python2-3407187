from fastapi import FastAPI
from modelos.clientes import Cliente
from modelos.facturas import Factura
from modelos.transacciones import Transaccion

app = FastAPI()

clientes = []
facturas = []
transacciones = []

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
    return {"mensaje": "Endpoint crear cliente"}


@app.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):
    return {"mensaje": "Endpoint actualizar cliente"}


@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    return {"mensaje": "Endpoint eliminar cliente"}


# ==========================
# FACTURAS
# ==========================

@app.get("/facturas")
def listar_facturas():
    return facturas


@app.post("/facturas")
def crear_factura(factura: Factura):
    return {"mensaje": "Endpoint crear factura"}


@app.put("/facturas/{id}")
def actualizar_factura(id: int, factura: Factura):
    return {"mensaje": "Endpoint actualizar factura"}


@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    return {"mensaje": "Endpoint eliminar factura"}


# ==========================
# TRANSACCIONES
# ==========================

@app.get("/transacciones")
def listar_transacciones():
    return transacciones


@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):
    return {"mensaje": "Endpoint crear transaccion"}


@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion: Transaccion):
    return {"mensaje": "Endpoint actualizar transaccion"}


@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    return {"mensaje": "Endpoint eliminar transaccion"}