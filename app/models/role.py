from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="roles")
