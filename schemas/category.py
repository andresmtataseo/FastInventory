from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(min_length=3, max_length=75)

class CategoryRead(CategoryBase):
    id: int

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass
