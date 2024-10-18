
import unittest
from scripts.anomaly_detection import detect_anomalies

class TestAnomalyDetection(unittest.TestCase):
    def test_detect_anomalies(self):
        anomalies = detect_anomalies([50, 120, 200], threshold=100)
        self.assertEqual(anomalies, [120, 200])

if __name__ == "__main__":
    unittest.main()
