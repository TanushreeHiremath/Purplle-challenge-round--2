from sqlalchemy import func

from services.api_service.database.models import Event
from services.api_service.database.session import SessionLocal


def calculate_conversion_rate(store_id: str):

    db = SessionLocal()

    try:

        total_visitors = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "ENTRY"
            )
            .distinct()
            .count()
        )

        purchased_visitors = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "PURCHASE"
            )
            .distinct()
            .count()
        )

        if total_visitors == 0:
            return 0

        return round(
            (purchased_visitors / total_visitors) * 100,
            2
        )

    finally:
        db.close()