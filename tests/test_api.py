
import unittest
from dashboard.dashboard import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
