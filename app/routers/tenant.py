from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/tenants",
    tags=["tenants"]
)

@router.post("/", response_model=schemas.tenant.Tenant)
def create_tenant(tenant: schemas.tenant.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = crud.tenant.create_tenant(db=db, tenant=tenant)
    return db_tenant

@router.get("/", response_model=List[schemas.tenant.Tenant])
def read_tenants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tenants = crud.tenant.get_tenants(db, skip=skip, limit=limit)
    return tenants

@router.get("/{tenant_id}", response_model=schemas.tenant.Tenant)
def read_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_tenant = crud.tenant.get_tenant(db, tenant_id=tenant_id)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant
