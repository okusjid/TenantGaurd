from pydantic import BaseModel
from typing import List

class Role(BaseModel):
    name: str

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: str
    tenant_id: int
    roles: List[Role] = []

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    tenant_id: int
