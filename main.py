from fastapi import FastAPI

app = FastAPI()

clientes = []

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.get("/clientes")
def listar_clientes():
    return clientes