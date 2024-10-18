
from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')  # Load YOLOv8 model

def detect_behavior_in_video(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            annotated_frame = results[0].plot()
            cv2.imshow('YOLOv8 Behavior Detection', annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error during behavior detection: {e}")
