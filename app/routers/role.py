from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@router.post("/", response_model=schemas.role.Role)
def create_role(role: schemas.role.RoleCreate, db: Session = Depends(get_db)):
    db_role = crud.role.create_role(db=db, role=role)
    return db_role

@router.get("/", response_model=List[schemas.role.Role])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    roles = crud.role.get_roles(db, skip=skip, limit=limit)
    return roles

@router.get("/{role_id}", response_model=schemas.role.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.role.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
