from sqlalchemy import Column, String, Integer
from database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(75), nullable=False)
