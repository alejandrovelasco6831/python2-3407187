# API Clientes - FastAPI

## Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando FastAPI para la gestión de Clientes, Facturas y Transacciones.

La aplicación implementa un CRUD completo para cada una de las entidades y utiliza SQLModel para la conexión con una base de datos SQLite.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- SQLModel
- SQLite
- Git
- GitHub
- Visual Studio Code

---

## Instalación

### Crear entorno virtual

```bash
python -m venv .mi_env
```

### Activar entorno virtual

Windows

```bash
.mi_env\Scripts\activate
```

### Instalar dependencias

```bash
pip install fastapi
pip install uvicorn
pip install sqlmodel
```

---

## Ejecutar el proyecto

```bash
uvicorn main:app --reload
```

Abrir en el navegador:

```
http://127.0.0.1:8000/docs
```

---

## Funcionalidades

### Clientes

- Crear cliente
- Listar clientes
- Buscar cliente
- Actualizar cliente
- Eliminar cliente

### Facturas

- Crear factura
- Listar facturas
- Actualizar factura
- Eliminar factura

### Transacciones

- Crear transacción
- Listar transacciones
- Actualizar transacción
- Eliminar transacción

---

## Base de datos

El proyecto utiliza SQLite mediante SQLModel.

Se implementan las siguientes entidades:

- Clientes
- Facturas
- Transacciones

Relaciones:

- Un cliente puede tener muchas facturas.
- Una factura puede tener muchas transacciones.

---

## Estructura del proyecto

```
python2-3407187/

│── database/
│── enrutadores/
│── modelos/
│── main.py
│── database.db
│── README.md
```

---

## Autor

Alejandro Velasco

---

## Repositorio

Repositorio desarrollado para el proyecto de FastAPI del SENA.