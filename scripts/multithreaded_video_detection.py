
import threading

def detect_in_frame(frame_id):
    """Simulate deepfake detection in a video frame."""
    print(f"Processing frame {frame_id}...")

if __name__ == "__main__":
    threads = [threading.Thread(target=detect_in_frame, args=(i,)) for i in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
