
import unittest
from scripts.gpu_optimization import infer_on_image

class TestDeepfakeDetection(unittest.TestCase):
    def test_infer_on_image(self):
        # Test with a simulated input (replace with actual path during testing)
        result = infer_on_image("test_images/fake_image.jpg")
        self.assertIn(result, ["Deepfake Detected", "Authentic Video"])

if __name__ == "__main__":
    unittest.main()
