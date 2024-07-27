from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)  # Specify length for VARCHAR
    users = relationship("User", back_populates="tenant")
