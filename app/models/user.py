from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    tenant_id = Column(Integer, ForeignKey("tenants.id"))

    tenant = relationship("Tenant", back_populates="users")
    roles = relationship("Role", back_populates="user")
