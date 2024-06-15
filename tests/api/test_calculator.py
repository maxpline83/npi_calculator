import unittest
from fastapi.testclient import TestClient
from src.api.app import app
from src.database.database import DatabaseConnector


class TestCalculatorRouter(unittest.TestCase):
    # TODO: Test with response status

    def setUp(self):
        self.client = TestClient(app)
        self.db_connector = DatabaseConnector(db_name="api_requests.db")

    def test_npi_calculator_success(self):
        expression = "3 5 +"
        expected_result = {"expression": "3 5 +", "result": 8}
        response = self.client.get(f"/calculator/npi_calculator/{expression}")
        self.assertEqual(response.json(), expected_result)

    def test_npi_calculator_error(self):
        expression = "3 0 ÷"
        expected_error = {"expression": "3 0 ÷", "error": "Division by zero is not allowed"}
        response = self.client.get(f"/calculator/npi_calculator/{expression}")
        self.assertEqual(response.json(), expected_error)


if __name__ == "__main__":
    unittest.main()
