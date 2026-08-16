from fastapi import APIRouter
router = APIRouter()
# get products 

@router.get("/")
async def get_products():
    return {"message": "All Products!"}

# get product by id
@router.get("/{product_id}")
async def get_product(product_id: int):
    return {"message": "All Products!"}

# post router
@router.post("/")
async def create_product():
    return {"message": "Product Created!"}