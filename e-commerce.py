from fastapi import FastAPI
from .routers import product, category, cart, order

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(category.router, prefix="/categories", tags=["categories"])
app.include_router(cart.router, prefix="/cart", tags=["cart"])
app.include_router(order.router, prefix="/orders", tags=["orders"])

