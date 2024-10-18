
import unittest
from scripts.multithreaded_video_detection import stream_video

class TestVideoStream(unittest.TestCase):
    def test_video_processing(self):
        # Simulate a video path input
        try:
            stream_video("test_videos/sample_video.mp4")
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
