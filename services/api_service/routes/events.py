from fastapi import APIRouter
from fastapi import HTTPException

from services.api_service.ingestion.event_ingestor import save_event
from services.api_service.ingestion.stream_consumer import publish_event
from shared.schemas.event_schema import EventSchema

router = APIRouter()


@router.post("/events/ingest")
async def ingest_event(event: EventSchema):

    inserted = save_event(event)

    if not inserted:
        raise HTTPException(
            status_code=409,
            detail="Duplicate event detected"
        )

    publish_event(event.model_dump(mode="json"))

    return {
        "status": "success",
        "event_id": str(event.event_id)
    }