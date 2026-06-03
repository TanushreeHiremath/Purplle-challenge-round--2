import supervision as sv
import numpy as np

from services.detection_service.trackers.base_tracker import (
    BaseTracker,
)


class ByteTrackerWrapper(BaseTracker):

    def __init__(self):

        self.tracker = sv.ByteTrack()

    def update(self, detections):

        if len(detections) == 0:
            return []

        xyxy = []
        confidence = []

        for det in detections:

            xyxy.append(det["bbox"])

            confidence.append(
                det["confidence"]
            )

        detections_sv = sv.Detections(
        xyxy=np.array(xyxy),
        confidence=np.array(confidence),class_id=np.array([0] * len(xyxy)))

        tracked = self.tracker.update_with_detections(
            detections_sv
        )

        tracks = []

        for i in range(len(tracked.xyxy)):

            tracks.append({
                "track_id": int(
                    tracked.tracker_id[i]
                ),
                "bbox": tracked.xyxy[i].astype(int).tolist(),
                "confidence": float(
                    tracked.confidence[i]
                )
            })

        return tracks