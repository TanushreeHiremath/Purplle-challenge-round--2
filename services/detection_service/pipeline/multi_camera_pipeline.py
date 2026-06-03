from services.detection_service.detectors.yolo_detector import (
    YOLODetector,
)

from services.detection_service.trackers.simple_tracker import (
    ByteTrackerWrapper,
)

from services.detection_service.pipeline.video_pipeline import (
    VideoPipeline,
)


CAMERA_VIDEOS = {

    "CAM_PRODUCT_01": "data/CAM1.mp4",

    "CAM_BROWSING_01": "data/CAM2.mp4",

    "CAM_ENTRY_01": "data/CAM3.mp4",

    "CAM_AUX_01": "data/CAM4.mp4",

    "CAM_BILLING_01": "data/CAM5.mp4",
}


def run_pipeline():

    detector = YOLODetector()

    tracker = ByteTrackerWrapper()

    pipeline = VideoPipeline(
        detector=detector,
        tracker=tracker
    )

    for camera_id, video_path in CAMERA_VIDEOS.items():

        print(
            f"\nStarting {camera_id}"
        )

        pipeline.process_video(
            video_path=video_path,
            camera_id=camera_id
        )

        print(
            f"Completed {camera_id}"
        )


if __name__ == "__main__":

    run_pipeline()