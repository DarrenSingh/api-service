from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, ValidationError

router = APIRouter()

products = [];

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str | None = None

# create new product
@router.post("/")
async def create_product(product: Product):
    try:
        if product.price < 0:
            raise ValueError("Price must be greater than 0")
        
        products.append(product.model_dump())
        return product

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.json())
    pass

# retrieve all products
@router.get("/")
async def get_products():
    return products

# retrieve single product
@router.get("/{id}")
async def get_product(id: int):
    try:
        return products[id - 1]
    except IndexError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not found')
    

# update product
@router.put("/{id}")
async def update_product(id: int, product: Product):
    try:
        if products[id - 1]:
            products[id - 1]  = Product
    except IndexError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not found')
    # product validations 

# delete product
@router.delete("/{id}")
async def delete_product(id: int):
    try:
        if products[id - 1]:
            products[id - 1]  = None
    except IndexError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not found')

