from fastapi import FastAPI
from modelos.clientes import Cliente

app = FastAPI()

# Lista temporal de clientes
clientes = []

# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

# Listar todos los clientes
@app.get("/clientes")
def listar_clientes():
    return clientes

# Listar un cliente por ID
@app.get("/clientes/{id}")
def listar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}

# Editar un cliente
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