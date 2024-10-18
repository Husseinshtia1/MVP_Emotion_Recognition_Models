
import unittest
from utils.vault_integration import store_secret

class TestHomomorphicEncryption(unittest.TestCase):
    def test_store_secret(self):
        result = store_secret("api_key", "12345")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
