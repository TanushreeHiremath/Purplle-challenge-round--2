import cv2
import numpy as np


def point_in_polygon(point, polygon):

    polygon_np = np.array(
        polygon,
        dtype=np.int32
    )

    return (
        cv2.pointPolygonTest(
            polygon_np,
            point,
            False
        ) >= 0
    )