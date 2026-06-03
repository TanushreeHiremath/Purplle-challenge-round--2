import json

import redis

from services.api_service.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)


def publish_event(event):
    redis_client.xadd(
        "store_events",
        {
            "data": json.dumps(event)
        }
    )