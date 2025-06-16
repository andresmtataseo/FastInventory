from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(min_length=3, max_length=75)
    price: float
    category_id: int

class ProductRead(ProductBase):
    sku: str

class ProductCreate(ProductBase):
    sku: str

class ProductUpdate(ProductBase):
    pass