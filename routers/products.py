from fastapi import APIRouter, Depends
from dependency import authenticate_user
router = APIRouter(dependencies=[Depends(authenticate_user)])
# get products


@router.get("/")
async def get_products():
    return {"message": "All Products!"}


# post router
@router.post("/")
async def create_product():
    return {"message": "Product Created!"}

# search router
@router.get("/search")
async def search_product(name: str):
    return {"message": "Searching Product!", "name": name}

# get product by id
@router.get("/{product_id}")
async def get_product(product_id: int):
    return {"message": "All Products!", "product_id": product_id}



