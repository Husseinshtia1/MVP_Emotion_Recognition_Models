
import unittest
from scripts.emotion_detection import detect_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_detect_emotion(self):
        self.assertEqual(detect_emotion("I feel great!"), "happy")
        self.assertEqual(detect_emotion("I am so sad."), "sad")

if __name__ == "__main__":
    unittest.main()
