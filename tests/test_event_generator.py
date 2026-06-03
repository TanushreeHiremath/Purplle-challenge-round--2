# PROMPT:
# Generate pytest unit tests for a retail analytics
# event generator producing schema-compliant events.

# CHANGES MADE:
# - Added ST1008 store validation
# - Added metadata assertions
# - Updated visitor token checks


from services.detection_service.events.event_generator import (
    build_event,
)


def test_event_schema():

    event = build_event(

        visitor_id=1,

        camera_id="CAM_ENTRY_01",

        event_type="ENTRY",

        confidence=0.91
    )

    assert "event_id" in event

    assert event["store_id"] == "ST1008"

    assert event["camera_id"] == "CAM_ENTRY_01"

    assert event["visitor_id"].startswith(
        "VIS_"
    )

    assert "metadata" in event

    assert "session_seq" in event[
        "metadata"
    ]