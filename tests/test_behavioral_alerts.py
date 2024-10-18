
import unittest
from scripts.behavioral_alert_integration import linked_alerts

class TestBehavioralAlerts(unittest.TestCase):
    def test_linked_alerts(self):
        # Simulate behavioral data and a deepfake detection flag
        try:
            linked_alerts(True, {"aggression": 0.8})
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
