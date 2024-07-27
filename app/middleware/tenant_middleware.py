from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        tenant_id = request.headers.get('X-Tenant-ID')
        if not tenant_id:
            return JSONResponse(status_code=400, content={"detail": "Tenant ID required"})
        request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
