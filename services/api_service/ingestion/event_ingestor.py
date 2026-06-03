from services.api_service.database.models import Event
from services.api_service.database.session import SessionLocal


def save_event(event_data):
    db = SessionLocal()

    try:
        existing_event = (
            db.query(Event)
            .filter(Event.event_id == str(event_data.event_id))
            .first()
        )

        if existing_event:
            return False

        db_event = Event(
            event_id=str(event_data.event_id),
            store_id=event_data.store_id,
            camera_id=event_data.camera_id,
            visitor_id=event_data.visitor_id,
            event_type=event_data.event_type,
            timestamp=event_data.timestamp,
            zone_id=event_data.zone_id,
            dwell_ms=event_data.dwell_ms,
            is_staff=event_data.is_staff,
            confidence=event_data.confidence
        )

        db.add(db_event)
        db.commit()

        return True

    finally:
        db.close()