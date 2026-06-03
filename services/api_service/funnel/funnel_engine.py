from services.api_service.database.models import Event
from services.api_service.database.session import SessionLocal


def calculate_funnel(store_id):

    db = SessionLocal()

    try:

        entered = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "ENTRY"
            )
            .distinct()
            .count()
        )

        browsed = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "ZONE_ENTER"
            )
            .distinct()
            .count()
        )

        queued = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "QUEUE_JOIN"
            )
            .distinct()
            .count()
        )

        purchased = (
            db.query(Event.visitor_id)
            .filter(
                Event.store_id == store_id,
                Event.event_type == "PURCHASE"
            )
            .distinct()
            .count()
        )

        return {
            "entered": entered,
            "browsed": browsed,
            "queued": queued,
            "purchased": purchased
        }

    finally:
        db.close()