import cv2
import json
from config.settings import ZONE_FILES
from core.utils import draw_zone

def save_zone_json(pointes):
    """ Chizilgan zone chegaralarnini nuqtalarini jsonga saqlash """
    with open(ZONE_FILES, "w") as f:
        json.dump({"zones": [pointes]}, f, indent=4)

def load_zone_json():
    """ Zone nuqtalarini json fayildan o'qib olish"""
    try:
        with open(ZONE_FILES, "r") as f:
            data = json.load(f)
            return data.get("zones", [])[0]
    except FileNotFoundError:
        return []

def draw_and_save_zone(video_path):
    """ Zonani chizish va saqlash"""
    read_video = cv2.VideoCapture(video_path)
    read, frame = read_video.read()
    read_video.release()
    if not read:
        print("Videoni o‘qib bo‘lmadi.")

    clone = frame.copy()
    points = []

    def draw_points(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))

    cv2.namedWindow("Draw Points")
    cv2.setMouseCallback("Draw Points", draw_points)

    while True:
        temp = clone.copy()
        draw_zone(temp, points)
        cv2.imshow("Draw Points", temp)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            points.clear()
        elif key == ord("c"):
            if len(points) > 2:
                save_zone_json(points)
                break
        elif key == 27:
            break
    cv2.destroyAllWindows()

