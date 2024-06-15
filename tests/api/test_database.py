import unittest
from fastapi.testclient import TestClient
from src.api.app import app
from src.database.database import DatabaseConnector

class TestDatabaseRouter(unittest.TestCase):
    # TODO: Test with response status
    def setUp(self):
        self.client = TestClient(app)
        self.db_connector = DatabaseConnector(db_name="api_requests.db")

    def test_get_history(self):
        response = self.client.get("/database/history")
        self.assertEqual(response.status_code, 200)

    def test_clear_history(self):
        response = self.client.get("/database/clear")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "DB Reset!")

    def test_export_to_csv(self):
        filename = "test_export.csv"
        response = self.client.get(f"/database/export_to_csv/{filename}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], f"Data exported to {filename}")


if __name__ == "__main__":
    unittest.main()
