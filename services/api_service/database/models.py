from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from services.api_service.database.session import Base


class Event(Base):
    __tablename__ = "events"

    event_id = Column(String, primary_key=True)

    store_id = Column(String, nullable=False)
    camera_id = Column(String, nullable=False)

    visitor_id = Column(String, nullable=False)

    event_type = Column(String, nullable=False)

    timestamp = Column(DateTime, nullable=False)

    zone_id = Column(String)

    dwell_ms = Column(Integer)

    is_staff = Column(Boolean, default=False)

    confidence = Column(Float, nullable=False)