from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.product import ProductRead, ProductCreate, ProductUpdate
from models.product import Product as ProductModel
from models.category import Category as CategoryModel

router = APIRouter()


@router.get('/products', response_model=list[ProductRead])
def get_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()


@router.post('/product', response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.sku == product.sku).first()
    if db_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un producto con el mismo SKU")

    db_category = db.query(CategoryModel).filter(CategoryModel.id == product.category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoria no existe")

    new_product = ProductModel(
        sku=product.sku,
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.put('/product/{product_sku}', response_model=ProductRead)
def update_product(product_sku: str, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.sku == product_sku).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El producto no existe")

    if product.category_id:
        db_category = db.query(CategoryModel).filter(CategoryModel.id == product.category_id).first()
        if not db_category:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoria no existe")

    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete('/product/{product_sku}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_sku: str, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.sku == product_sku).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El producto no existe")

    db.delete(db_product)
    db.commit()
    return {"message": "El producto fue eliminado"}