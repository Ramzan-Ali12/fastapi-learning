from fastapi import FastAPI
from routers import products

API_PREFIX = "/api/v1"
app = FastAPI()
app.include_router(products.router,tags=["Products"],prefix=f"{API_PREFIX}/products")