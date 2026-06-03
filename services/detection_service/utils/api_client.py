import json
import requests


API_URL = (
    "http://localhost:8000/events/ingest"
)


def send_event(event):

    try:

        print("\n================ EVENT ================\n")

        print(
           f"[EVENT] "
    f"{event['event_type']} | "
    f"{event['visitor_id']}"
        )

        response = requests.post(
            API_URL,
            json=event,
            timeout=5
        )

        print(
            f"\nEvent sent: {response.status_code}\n"
        )

        with open(
            "logs/events.jsonl",
            "a"
        ) as f:

            f.write(
                json.dumps(event)
                + "\n"
            )

    except Exception as e:

        print(
            "Failed to send event:",
            e
        )