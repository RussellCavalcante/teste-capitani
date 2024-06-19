from pydantic import BaseModel, Field
from typing import Dict

class Pricing(BaseModel):
    amount: float
    currency: str

class Availability(BaseModel):
    quantity: int
    timestamp: str

class ProductBase(BaseModel):
    id: str
    name: str
    description: str
    pricing: Pricing
    availability: Availability
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    class Config:
        orm_mode = True
