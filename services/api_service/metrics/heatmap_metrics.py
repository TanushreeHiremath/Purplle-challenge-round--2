from sqlalchemy import func

from services.api_service.database.models import Event
from services.api_service.database.session import SessionLocal


def get_zone_heatmap(store_id: str):

    db = SessionLocal()

    try:

        results = (
            db.query(
                Event.zone_id,
                func.count().label("count")
            )
            .filter(
                Event.store_id == store_id,
                Event.zone_id.isnot(None)
            )
            .group_by(Event.zone_id)
            .all()
        )

        return {
            row.zone_id: row.count
            for row in results
        }

    finally:
        db.close()