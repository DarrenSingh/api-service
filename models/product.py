from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str | None = None