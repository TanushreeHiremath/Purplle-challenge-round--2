from fastapi import APIRouter

from services.api_service.metrics.heatmap_metrics import get_zone_heatmap

router = APIRouter()


@router.get("/stores/{store_id}/heatmap")
async def heatmap(store_id: str):

    return get_zone_heatmap(store_id)