from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EventSchema(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)

    store_id: str
    camera_id: str
    visitor_id: str

    event_type: str

    timestamp: datetime

    zone_id: Optional[str] = None

    dwell_ms: Optional[int] = None

    is_staff: bool = False

    confidence: float