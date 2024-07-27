from sqlalchemy.orm import Session
from app import models, schemas
from app.auth.security import get_password_hash

def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.user.User(username=user.username, email=user.email, hashed_password=hashed_password, tenant_id=user.tenant_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.user.User).offset(skip).limit(limit).all()
