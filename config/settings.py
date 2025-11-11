from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ZONE_FILES = BASE_DIR / "restricted_sone.json"
MODEL_PATH = BASE_DIR / "yolov8n.pt"
ALARM_DURATION = 3