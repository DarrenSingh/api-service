from fastapi import APIRouter

router = APIRouter()

# create new order from shopping cart
@router.post("/")
async def create_order():
    # ... implement
    pass
