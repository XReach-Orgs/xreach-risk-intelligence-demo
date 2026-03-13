from fastapi import FastAPI
from sqlalchemy import text

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.security import generic_exception_handler
from app.db.base import Base
from app.db.session import engine
from app.observability.middleware import MetricsMiddleware

configure_logging()
settings = get_settings()

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.add_exception_handler(Exception, generic_exception_handler)
app.add_middleware(MetricsMiddleware)
app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/")
def root():
    return {"service": settings.app_name, "environment": settings.environment}


@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database": "ok"}