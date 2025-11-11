import cv2
import time
from ultralytics import YOLO
from core.zone_manager import load_zone_json
from core.utils import draw_zone, is_point_in_zone
from config.settings import MODEL_PATH, ALARM_DURATION

def detect_intrusion(video_path):
    """ Odam zonaga kirsa xabar chiqarish """
    zone = load_zone_json()
    if not zone:
        print("Zona aniqlanmagan. Avval --draw rejimida chizing.")
        return

    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(video_path)
    alarm_active = False
    last_alarm_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, classes=[0])
        draw_zone(frame, zone)

        intrusion = False

        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)
                if is_point_in_zone((cx, cy), zone):
                    intrusion = True
                    break

        if intrusion:
            alarm_active = True
            last_alarm_time = time.time()

        elif alarm_active and time.time() - last_alarm_time > ALARM_DURATION:
            alarm_active = False

        if alarm_active:
            cv2.putText(
                frame, "ALARM!", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4
            )

        cv2.imshow("Restricted Zone Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()