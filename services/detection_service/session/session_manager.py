from datetime import datetime

from services.detection_service.session.visitor_state_machine import VisitorState


class VisitorSession:

    def __init__(self, visitor_id: str):

        self.visitor_id = visitor_id

        self.current_state = VisitorState.ENTERED_STORE

        self.entry_time = datetime.utcnow()

        self.last_seen = datetime.utcnow()

        self.current_zone = None

        self.total_dwell_time = 0

        self.visited_zones = []

        self.queue_joined = False

        self.purchase_completed = False

    def update_zone(self, zone_id: str):

        self.current_zone = zone_id

        self.last_seen = datetime.utcnow()

        if zone_id not in self.visited_zones:
            self.visited_zones.append(zone_id)

        self.current_state = VisitorState.ZONE_INTERACTION

    def join_queue(self):

        self.queue_joined = True

        self.current_state = VisitorState.BILLING_QUEUE

    def complete_purchase(self):

        self.purchase_completed = True

        self.current_state = VisitorState.PURCHASED

    def abandon_queue(self):

        self.current_state = VisitorState.ABANDONED

    def exit_store(self):

        self.current_state = VisitorState.EXITED

    def get_session_summary(self):

        return {
            "visitor_id": self.visitor_id,
            "current_state": self.current_state,
            "visited_zones": self.visited_zones,
            "purchase_completed": self.purchase_completed,
            "queue_joined": self.queue_joined
        }