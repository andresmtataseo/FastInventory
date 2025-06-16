from fastapi import FastAPI
from routes.product import router as products_router
from routes.category import router as categories_router
from database import create_database_if_not_exists

app = FastAPI()

app.title = 'FastInventory'
app.description = 'REST API para administrar productos'
app.version = '1.0.0'

@app.on_event("startup")
async def startup_event():
    print("Iniciando la aplicación FastInventory...")
    create_database_if_not_exists()
    print("La base de datos y las tablas están listas.")

app.include_router(products_router)
app.include_router(categories_router)

@app.get("/")
async def read_root():
    return {"message": "Bienvenido FastInventory API!"}