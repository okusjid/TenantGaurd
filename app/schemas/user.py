from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    tenant_id: int

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
