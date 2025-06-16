from fastapi import FastAPI
from routes.product import router as products_router
from routes.category import router as categories_router

app = FastAPI()

app.title = 'FastInventory'
app.description = 'REST API para administrar productos'
app.version = '1.0.0'

app.include_router(products_router)
app.include_router(categories_router)