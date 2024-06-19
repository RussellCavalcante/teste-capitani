from sqlalchemy import Column, String, Float, Integer, JSON
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    pricing = Column(JSON)
    availability = Column(JSON)
    category = Column(String)
