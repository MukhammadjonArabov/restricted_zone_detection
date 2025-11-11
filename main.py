import argparse
from core.zone_manager import draw_and_save_zone
from core.detector import crossing_message

def main():
    parser = argparse.ArgumentParser(description="Restricted Zone Detection System")
    parser.add_argument("--video", "-v", required=True, help="Video fayl manzili")
    parser.add_argument("--draw", action="store_true", help="Zonani chizish rejimi")
    args = parser.parse_args()

    if args.draw:
        draw_and_save_zone(args.video)
    else:
        crossing_message(args.video)

if __name__ == "__main__":
    main()
