from collections import defaultdict
from datetime import datetime

from services.detection_service.utils.zone_utils import (
    point_in_polygon,
)

from services.detection_service.zones.zone_config import (
    ZONE_CONFIG,
)


QUEUE_TIMERS = defaultdict(dict)


def analyze_queue(
    camera_id,
    track_id,
    bbox
):

    if camera_id != "CAM5":
        return None

    queue_zone = (
        ZONE_CONFIG["CAM5"]["queue_zone"]
    )

    x1, y1, x2, y2 = bbox

    center_point = (
        int((x1 + x2) / 2),
        int((y1 + y2) / 2)
    )

    inside_queue = point_in_polygon(
        center_point,
        queue_zone
    )

    visitor_state = (
        QUEUE_TIMERS[track_id]
    )

    # ==========================
    # QUEUE JOIN
    # ==========================

    if inside_queue:

        if "joined_at" not in visitor_state:

            visitor_state[
                "joined_at"
            ] = datetime.utcnow()

            return {
                "event_type": "QUEUE_JOIN",
                "queue_wait_ms": 0
            }

    # ==========================
    # QUEUE EXIT
    # ==========================

    else:

        if "joined_at" in visitor_state:

            joined_at = visitor_state.pop(
                "joined_at"
            )

            wait_ms = int(
                (
                    datetime.utcnow()
                    - joined_at
                ).total_seconds() * 1000
            )

            return {
                "event_type": "QUEUE_EXIT",
                "queue_wait_ms": wait_ms
            }

    return None