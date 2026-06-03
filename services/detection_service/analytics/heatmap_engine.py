import numpy as np
import cv2


HEATMAP_POINTS = []


def update_heatmap(frame, bbox):

    x1, y1, x2, y2 = bbox

    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)

    HEATMAP_POINTS.append(
        (center_x, center_y)
    )

    heatmap = np.zeros(
        (frame.shape[0], frame.shape[1]),
        dtype=np.float32
    )

    for point in HEATMAP_POINTS:

        cv2.circle(
            heatmap,
            point,
            25,
            1,
            -1
        )

    heatmap = cv2.GaussianBlur(
        heatmap,
        (51, 51),
        0
    )

    heatmap = np.clip(
        heatmap * 10,
        0,
        255
    ).astype(np.uint8)

    colored_heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        frame,
        0.7,
        colored_heatmap,
        0.3,
        0
    )

    return overlay