import cv2
import time

from services.detection_service.events.entry_exit_events import (
    detect_entry_exit,
)

from services.detection_service.events.event_generator import (
    build_event,
)

from services.detection_service.events.zone_events import (
    detect_zone_event,
)

from services.detection_service.analytics.queue_engine import (
    analyze_queue,
)

from services.detection_service.analytics.purchase_engine import (
    detect_purchase,
)

from services.detection_service.utils.api_client import (
    send_event,
)

from services.detection_service.utils.logger import (
    logger,
)


class VideoPipeline:

    def __init__(
        self,
        detector,
        tracker
    ):

        self.detector = detector

        self.tracker = tracker

    def process_video(
        self,
        video_path,
        camera_id
    ):

        cap = cv2.VideoCapture(
            video_path
        )

        # ====================================
        # VIDEO OPEN CHECK
        # ====================================

        if not cap.isOpened():

            print(
                f"FAILED TO OPEN: {video_path}"
            )

            return

        print(
            f"SUCCESSFULLY OPENED: {video_path}"
        )

        frame_count = 0

        prev_time = time.time()

        while True:

            ret, frame = cap.read()

            if not ret:

                print(
                    f"Finished processing: {camera_id}"
                )

                break

            # ====================================
            # FRAME SKIPPING
            # ====================================

            frame_count += 1

            if frame_count % 3 != 0:
                continue

            # ====================================
            # DETECTION
            # ====================================

            detections = (
                self.detector.detect(frame)
            )

            # ====================================
            # TRACKING
            # ====================================

            tracks = (
                self.tracker.update(
                    detections
                )
            )

            for track in tracks:

                x1, y1, x2, y2 = (
                    track["bbox"]
                )

                # ====================================
                # ENTRY / EXIT EVENTS
                # ====================================

                event = None

                if camera_id == "CAM_ENTRY_01":

                    event = detect_entry_exit(
                        track["track_id"],
                        track["bbox"]
                    )

                if event:

                    event_payload = build_event(
                        visitor_id=track["track_id"],
                        camera_id=camera_id,
                        event_type=event,
                        confidence=track["confidence"]
                    )

                    send_event(
                        event_payload
                    )

                # ====================================
                # ZONE EVENTS
                # ====================================

                zone_event = detect_zone_event(
                    camera_id=camera_id,
                    track_id=track["track_id"],
                    bbox=track["bbox"]
                )

                if zone_event:

                    event_payload = build_event(
                        visitor_id=track["track_id"],
                        camera_id=camera_id,
                        event_type=zone_event["event_type"],
                        confidence=track["confidence"],
                        zone_id=zone_event["zone_id"],
                        dwell_ms=zone_event.get(
                            "dwell_ms",
                            0
                        )
                    )

                    send_event(
                        event_payload
                    )

                # ====================================
                # QUEUE ANALYTICS
                # ====================================

                queue_event = analyze_queue(
                    camera_id=camera_id,
                    track_id=track["track_id"],
                    bbox=track["bbox"]
                )

                if queue_event:

                    event_payload = build_event(
                        visitor_id=track["track_id"],
                        camera_id=camera_id,
                        event_type=queue_event["event_type"],
                        confidence=track["confidence"],
                        zone_id="queue_zone",
                        dwell_ms=queue_event.get(
                            "queue_wait_ms",
                            0
                        )
                    )

                    send_event(
                        event_payload
                    )

                    purchase_event = detect_purchase(
                        queue_event
                    )

                    if purchase_event:

                        purchase_payload = build_event(
                            visitor_id=track["track_id"],
                            camera_id=camera_id,
                            event_type=purchase_event["event_type"],
                            confidence=track["confidence"],
                            zone_id="billing_zone"
                        )

                        send_event(
                            purchase_payload
                        )

                # ====================================
                # HEATMAP DISABLED
                # ====================================

                pass

                # ====================================
                # DRAW BOX
                # ====================================

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f'ID {track["track_id"]}',
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

            # ====================================
            # ENTRY LINE
            # ====================================

            if camera_id == "CAM_ENTRY_01":

                cv2.line(
                    frame,
                    (1150, 0),
                    (1150, 1080),
                    (0, 0, 255),
                    3
                )

            # ====================================
            # FPS
            # ====================================

            current_time = time.time()

            fps = 1 / (
                current_time - prev_time
            )

            prev_time = current_time

            cv2.putText(
                frame,
                f"FPS: {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Camera: {camera_id}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            # ====================================
            # DISPLAY
            # ====================================

            cv2.imshow(
                f"Detection Pipeline - {camera_id}",
                frame
            )

            time.sleep(0.03)

            # ====================================
            # KEY HANDLING
            # ====================================

            key = cv2.waitKey(1)

            if key & 0xFF == ord('q'):

                break

        # ====================================
        # CLEANUP
        # ====================================

        cap.release()

        cv2.destroyWindow(
            f"Detection Pipeline - {camera_id}"
        )

        cv2.destroyAllWindows()