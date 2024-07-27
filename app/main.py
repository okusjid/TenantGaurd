from fastapi import FastAPI
from app.routers import user, tenant, role, auth
from app.middleware.tenant_middleware import TenantMiddleware
from app.database import engine
from app.models import user as user_model, tenant as tenant_model, role as role_model

app = FastAPI()

# Create all models
user_model.Base.metadata.create_all(bind=engine)
tenant_model.Base.metadata.create_all(bind=engine)
role_model.Base.metadata.create_all(bind=engine)

# Add Middleware
app.add_middleware(TenantMiddleware)

# Include Routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(tenant.router)
app.include_router(role.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the MultiTenant Project"}
