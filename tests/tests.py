import requests
import unittest

class TestFlaskAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5001"

    def test_get_customers(self):
        response = requests.get(f"{self.BASE_URL}/customers")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()