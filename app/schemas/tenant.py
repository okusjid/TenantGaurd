from pydantic import BaseModel

class Tenant(BaseModel):
    name: str

    class Config:
        orm_mode = True

class TenantCreate(BaseModel):
    name: str
