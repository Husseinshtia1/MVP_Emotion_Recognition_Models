
import unittest
from dashboard.dashboard import app

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
