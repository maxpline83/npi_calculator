from src.database.database import DatabaseConnector

DB_NAME = "api_requests.db"
db_connector = DatabaseConnector(db_name=DB_NAME)
db_connector.initialize_database()


def get_db_connector():
    return db_connector
