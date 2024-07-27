from sqlalchemy.orm import Session
from app import models, schemas

def create_tenant(db: Session, tenant: schemas.tenant.TenantCreate):
    db_tenant = models.tenant.Tenant(name=tenant.name)
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def get_tenant(db: Session, tenant_id: int):
    return db.query(models.tenant.Tenant).filter(models.tenant.Tenant.id == tenant_id).first()

def get_tenants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.tenant.Tenant).offset(skip).limit(limit).all()
