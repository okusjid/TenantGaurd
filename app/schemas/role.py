from pydantic import BaseModel

class Role(BaseModel):
    name: str

    class Config:
        from_attributes = True

class RoleCreate(BaseModel):
    name: str
    user_id: int
