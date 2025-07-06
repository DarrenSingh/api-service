from pydantic import BaseModel 

class OrderItem(BaseModel):
    order_id: int
    product_id:int
    quantity: int