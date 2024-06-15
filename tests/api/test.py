import unittest
from fastapi.testclient import TestClient
from src.api.app import app


class TestBasicApiRout(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.json(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
