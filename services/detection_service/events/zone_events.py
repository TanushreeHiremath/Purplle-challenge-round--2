from collections import defaultdict
from datetime import datetime

from services.detection_service.utils.zone_utils import (
    point_in_polygon,
)

from services.detection_service.zones.zone_config import (
    ZONE_CONFIG,
)


ZONE_TIMERS = defaultdict(dict)


def detect_zone_event(
    camera_id,
    track_id,
    bbox
):

    if camera_id not in ZONE_CONFIG:
        return None

    camera_config = (
        ZONE_CONFIG[camera_id]
    )

    x1, y1, x2, y2 = bbox

    center_point = (
        int((x1 + x2) / 2),
        int((y1 + y2) / 2)
    )

    for zone_name, polygon in camera_config.items():

        if (
            zone_name == "frame_size"
            or "line" in zone_name
        ):
            continue

        inside = point_in_polygon(
            center_point,
            polygon
        )

        visitor_zones = (
            ZONE_TIMERS[track_id]
        )

        if inside:

            if zone_name not in visitor_zones:

                visitor_zones[
                    zone_name
                ] = datetime.utcnow()

                return {
                    "event_type": "ZONE_ENTER",
                    "zone_id": zone_name
                }

        else:

            if zone_name in visitor_zones:

                start_time = (
                    visitor_zones.pop(
                        zone_name
                    )
                )

                dwell_ms = int(
                    (
                        datetime.utcnow()
                        - start_time
                    ).total_seconds() * 1000
                )

                return {
                    "event_type": "ZONE_EXIT",
                    "zone_id": zone_name,
                    "dwell_ms": dwell_ms
                }

    return None