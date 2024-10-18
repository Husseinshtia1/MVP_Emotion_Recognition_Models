
import cv2

def start_camera(device_index=0):
    '''Start a video stream from the specified device (e.g., mobile, laptop).'''
    cap = cv2.VideoCapture(device_index)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Live Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
