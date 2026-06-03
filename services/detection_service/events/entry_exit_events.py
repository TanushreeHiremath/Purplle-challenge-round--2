TRACK_HISTORY = {}

EVENT_COOLDOWN = {}


def get_center(bbox):

    x1, y1, x2, y2 = bbox

    return (
        int((x1 + x2) / 2),
        int((y1 + y2) / 2)
    )


def detect_entry_exit(
    track_id,
    bbox,
    entry_x=1150,
    cooldown_frames=50
):

    center_x, center_y = get_center(
        bbox
    )

    previous = TRACK_HISTORY.get(
        track_id
    )

    TRACK_HISTORY[track_id] = (
        center_x,
        center_y
    )

    if previous is None:
        return None

    prev_x, prev_y = previous

    # Cooldown check
    last_event_frame = EVENT_COOLDOWN.get(
        track_id,
        -9999
    )

    current_frame = len(TRACK_HISTORY)

    if (
        current_frame - last_event_frame
        < cooldown_frames
    ):

        return None

    # LEFT → RIGHT = ENTRY
    if (
        prev_x < entry_x
        and center_x >= entry_x
    ):

        EVENT_COOLDOWN[track_id] = current_frame

        return "ENTRY"

    # RIGHT → LEFT = EXIT
    if (
        prev_x > entry_x
        and center_x <= entry_x
    ):

        EVENT_COOLDOWN[track_id] = current_frame

        return "EXIT"

    return None