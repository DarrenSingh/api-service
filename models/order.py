from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    user_id: int
    order_date: datetime
    order_total: float