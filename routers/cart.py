from fastapi import APIRouter

router = APIRouter()

# create new shopping cart, or retrieve existing shopping cart
@router.post("/")
async def create_or_get_cart():
    # ... implement
    pass

# add product to shopping cart
@router.post("/{product_id}")
async def add_product_to_cart(product_id: int):
    # ... implement
    pass

# remove product from shopping cart
@router.delete("/{product_id}")
async def remove_product_from_cart(product_id: int):
    # ... implement
    pass

# retrieve all products in shopping cart
@router.get("/")
async def get_cart_products():
    # ... implement
    pass
