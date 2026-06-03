from fastapi import APIRouter

from services.api_service.metrics.conversion_metrics import (
    calculate_conversion_rate,
)

router = APIRouter()


@router.get("/stores/{store_id}/metrics")
async def get_store_metrics(store_id: str):

    conversion_rate = calculate_conversion_rate(store_id)

    return {
        "store_id": store_id,

        # Real implemented metric
        "conversion_rate": conversion_rate,

        # Placeholder metrics (implemented later)
        "visitors": 0,
        "avg_dwell_time": 0,
        "queue_depth": 0
    }