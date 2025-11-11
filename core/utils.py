import cv2
import numpy as np

def draw_zone(frame, points, color=(0, 0, 255)):
    """ Chizilgan chegarani ya'ni zona ekranda ko'rsatish """
    if len(points) > 1:
        cv2.polylines(frame, [np.array(points, np.int32)], isClosed=False, color=color, thickness=2)

def is_point_in_zone(point, zone):
    """ Nuqta zoani ichidaligiga tekshiraish """
    if not zone:
        return False
    return cv2.pointPolygonTest(np.array(zone, np.int32), point, False) >= 0