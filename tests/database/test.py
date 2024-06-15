import unittest
from src.database.database import DatabaseConnector

TEST_DB_NAME = 'test_api_requests.db'


class TestDatabaseConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the DatabaseConnector for testing
        cls.db_connector = DatabaseConnector(db_name=TEST_DB_NAME)
        cls.db_connector.initialize_database()

    def setUp(self):
        self.db_connector.insert_example_data_db()

    def test_insert_and_read_data(self):
        results = self.db_connector.read_db()
        self.assertEqual(len(results), 3)

        self.assertEqual(results[0].query, '5 3 +')
        self.assertEqual(results[0].result, 8.0)

        self.assertEqual(results[1].query, '4 2 * 3 +')
        self.assertEqual(results[1].result, 11.0)

        self.assertEqual(results[2].query, '10 2 ÷')
        self.assertEqual(results[2].result, 5.0)

    def test_remove_all_data(self):

        self.db_connector.remove_all_data_db()
        results = self.db_connector.read_db()
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()
