from fastapi import APIRouter

from services.api_service.funnel.funnel_engine import (
    calculate_funnel,
)

router = APIRouter()


@router.get("/stores/{store_id}/funnel")
async def get_funnel(store_id: str):

    return calculate_funnel(store_id)