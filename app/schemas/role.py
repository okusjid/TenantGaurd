from pydantic import BaseModel

class Role(BaseModel):
    name: str

    class Config:
        orm_mode = True

class RoleCreate(BaseModel):
    name: str
    user_id: int
