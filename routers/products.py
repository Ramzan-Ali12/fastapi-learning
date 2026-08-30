from fastapi import APIRouter, Depends

from dependency import  get_current_user


router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.get("/")
async def get_products():
    return {
        "message": "All Products!"
    }


@router.post("/")
async def create_product():
    return {
        "message": "Product Created!"
    }


@router.get("/search")
async def search_product(name: str):
    return {
        "message": "Searching Product!",
        "name": name
    }


@router.get("/{product_id}")
async def get_product(product_id: int):
    return {
        "message": "All Products!",
        "product_id": product_id
    }