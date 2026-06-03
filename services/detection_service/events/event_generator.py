import os
import uuid
import hashlib

from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


STORE_ID = os.getenv(
    "STORE_ID",
    "STORE_BLR_002"
)


VISITOR_SESSIONS = {}


def generate_visitor_token(
    visitor_id,
    camera_id
):

    raw = f"{visitor_id}_{camera_id}"

    hashed = hashlib.md5(
        raw.encode()
    ).hexdigest()[:6]

    return f"VIS_{hashed}"


def get_session_sequence(
    visitor_token
):

    if visitor_token not in VISITOR_SESSIONS:

        VISITOR_SESSIONS[
            visitor_token
        ] = 1

    else:

        VISITOR_SESSIONS[
            visitor_token
        ] += 1

    return VISITOR_SESSIONS[
        visitor_token
    ]


def build_event(
    visitor_id,
    camera_id,
    event_type,
    confidence,
    zone_id=None,
    dwell_ms=0,
    queue_depth=None,
    sku_zone=None,
    is_staff=False
):

    # ====================================
    # VISITOR TOKEN
    # ====================================

    visitor_token = (
        generate_visitor_token(
            visitor_id,
            camera_id
        )
    )

    # ====================================
    # SESSION SEQUENCE
    # ====================================

    session_seq = (
        get_session_sequence(
            visitor_token
        )
    )

    # ====================================
    # EVENT OBJECT
    # ====================================

    event = {

        "event_id": str(
            uuid.uuid4()
        ),

        "store_id": STORE_ID,

        "camera_id": camera_id,

        "visitor_id": visitor_token,

        "event_type": event_type,

        "timestamp": (
            datetime.utcnow()
            .replace(microsecond=0)
            .isoformat()
            + "Z"
        ),

        "zone_id": zone_id,

        "dwell_ms": int(
            dwell_ms
        ),

        "is_staff": bool(
            is_staff
        ),

        "confidence": round(
            float(confidence),
            2
        ),

        "metadata": {

            "queue_depth": queue_depth,

            "sku_zone": sku_zone,

            "session_seq": session_seq
        }
    }

    return event