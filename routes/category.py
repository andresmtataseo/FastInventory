from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from models.category import Category as CategoryModel
from models.product import Product as ProductModel

router = APIRouter()


@router.get('/categories', response_model=list[CategoryRead])
def get_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()


@router.post('/category', response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.name == category.name).first()
    if db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de la categoria ya existe")

    new_category = CategoryModel(
        name=category.name,
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.put('/category/{category_id}', response_model=CategoryRead)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria no existe")

    category_name = db.query(CategoryModel).filter(
        CategoryModel.name == category.name,
        CategoryModel.id != category_id
    ).first()
    if category_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Ya existe una categoria con el mismo nombre")

    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria no existe")

    dependent_products = db.query(ProductModel).filter(ProductModel.category_id == category_id).first()
    if dependent_products:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="No se puede eliminar la categoria porque hay productos asociados a ella")

    db.delete(db_category)
    db.commit()
    return {"message": "La categoria fue eliminada"}