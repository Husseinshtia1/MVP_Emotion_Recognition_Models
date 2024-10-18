
import cv2
import dlib
import random
import time

# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def monitor_physiological_data(video_source=0):
    cap = cv2.VideoCapture(video_source)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            landmarks = predictor(gray, face)
            cv2.circle(frame, (landmarks.part(36).x, landmarks.part(36).y), 2, (0, 255, 0), -1)
            cv2.circle(frame, (landmarks.part(45).x, landmarks.part(45).y), 2, (0, 255, 0), -1)
            heart_rate = random.randint(60, 100)  # Simulate heart rate
            stress_level = random.uniform(0.0, 1.0)  # Simulate stress level
            print(f"Heart Rate: {heart_rate} bpm, Stress Level: {stress_level}")
        cv2.imshow("Physiological Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
