from sqlalchemy.orm import Session
from app import models, schemas

def create_role(db: Session, role: schemas.role.RoleCreate):
    db_role = models.role.Role(name=role.name, user_id=role.user_id)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(models.role.Role).filter(models.role.Role.id == role_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.role.Role).offset(skip).limit(limit).all()
