from fastapi import FastAPI
from enrutadores import clientes
from enrutadores import facturas
from enrutadores import transacciones

app = FastAPI()

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}