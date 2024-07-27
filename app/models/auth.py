from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel


class Token(BaseModel):
    __tablename__ = "tokken"
    access_token: Column(String, primary_key=True, index=True)
    token_type: Column(String, unique=True, index=True)
