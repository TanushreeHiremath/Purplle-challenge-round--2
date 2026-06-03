from fastapi import FastAPI

from services.api_service.database.models import Base
from services.api_service.database.session import engine
from services.api_service.routes.events import router as event_router
from services.api_service.routes.metrics import router as metrics_router
from services.api_service.routes.funnel import router as funnel_router
from services.api_service.routes.heatmap import router as heatmap_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence Platform",
    version="1.0.0"
)

app.include_router(event_router)
app.include_router(metrics_router)
app.include_router(funnel_router)
app.include_router(heatmap_router)

@app.get("/")
async def root():
    return {
        "message": "Store Intelligence Platform API Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }