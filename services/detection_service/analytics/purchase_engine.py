from datetime import datetime

from services.detection_service.analytics.pos_engine import (
    match_pos_transaction,
)


def detect_purchase(
    queue_event
):

    if (
        queue_event["event_type"]
        != "QUEUE_EXIT"
    ):

        return None

    event_time = datetime.utcnow()

    pos_match = match_pos_transaction(
        event_time
    )

    if pos_match["matched"]:

        return {
            "event_type": "PURCHASE",
            "transaction_id": pos_match[
                "transaction_id"
            ],
            "amount": pos_match[
                "amount"
            ]
        }

    return {
        "event_type": "QUEUE_ABANDON"
    }