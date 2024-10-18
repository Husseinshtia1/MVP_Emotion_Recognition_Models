
import unittest
from scripts.authentication import authenticate_user

class TestAuthentication(unittest.TestCase):
    def test_valid_credentials(self):
        self.assertTrue(authenticate_user("admin", "password123"))

if __name__ == "__main__":
    unittest.main()
