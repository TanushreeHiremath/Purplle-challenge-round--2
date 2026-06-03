from ultralytics import YOLO

from services.detection_service.detectors.base_detector import (
    BaseDetector,
)


class YOLODetector(BaseDetector):

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(
            frame,
            classes=[0],
            verbose=False,
            imgsz=640,
            conf=0.4
        )

        detections = []

        for result in results:

            for box in result.boxes:

                x1, y1, x2, y2 = (
                    box.xyxy[0]
                    .cpu()
                    .numpy()
                )

                confidence = (
                    float(box.conf[0])
                )

                detections.append({
                    "bbox": [
                        int(x1),
                        int(y1),
                        int(x2),
                        int(y2)
                    ],
                    "confidence": confidence
                })

        return detections