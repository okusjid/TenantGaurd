from pydantic import BaseModel

class Tenant(BaseModel):
    name: str

    class Config:
        from_attributes = True

class TenantCreate(BaseModel):
    name: str
