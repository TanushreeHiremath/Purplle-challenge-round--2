from enum import Enum


class VisitorState(str, Enum):
    ENTERED_STORE = "ENTERED_STORE"

    BROWSING = "BROWSING"

    ZONE_INTERACTION = "ZONE_INTERACTION"

    BILLING_QUEUE = "BILLING_QUEUE"

    PURCHASED = "PURCHASED"

    ABANDONED = "ABANDONED"

    EXITED = "EXITED"