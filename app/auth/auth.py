from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.jwt_handler.py import create_access_token, get_current_user
from app.dependencies import get_db
from app.models.user import User
from app.auth.security import verify_password

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
