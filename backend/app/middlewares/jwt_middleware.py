from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.security import verify_token


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/admin"):
            # Пробуем сначала заголовок Authorization
            auth_header = request.headers.get("Authorization")
            token = None

            if auth_header and auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
            else:
                # Пытаемся взять токен из query-параметра
                token = request.query_params.get("token")

            if not token:
                raise HTTPException(status_code=401, detail="Missing or invalid token")

            if not verify_token(token):
                raise HTTPException(status_code=401, detail="Invalid or expired token")

        response = await call_next(request)
        return response
