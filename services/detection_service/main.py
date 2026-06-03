from services.detection_service.detectors.yolo_detector import (
    YOLODetector,
)

from services.detection_service.pipeline.video_pipeline import (
    VideoPipeline,
)

from services.detection_service.trackers.simple_tracker import (
    ByteTrackerWrapper,
)


def main():

    detector = YOLODetector()

    tracker = ByteTrackerWrapper()

    pipeline = VideoPipeline(
        detector,
        tracker
    )

    pipeline.process_video(
        "data/CAM3.mp4"
    )


if __name__ == "__main__":
    main()