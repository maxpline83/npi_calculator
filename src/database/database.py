from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


class DatabaseConnector:
    """
    A class to connect to a SQLite database and perform operations on it.
    
    Attributes:
        db_name (str): The name of the database.
        db_path (str): The path to the database.
        engine (sqlalchemy.engine.base.Engine): The engine to connect to the database.
        Base (sqlalchemy.ext.declarative.api.DeclarativeMeta): The base class for the database model.
        Session (sqlalchemy.orm.session.sessionmaker): The session class for the database.
        model (sqlalchemy.ext.declarative.api.DeclarativeMeta): The model class for the database.
    """
    def __init__(self, db_name):
        self.db_name = db_name
        os.makedirs("data/database/", exist_ok=True)
        self.db_path = f'sqlite:///data/database/{db_name}'
        self.engine = create_engine(self.db_path, echo=True)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.model = self.create_model()
        print("Database connected successfully.")

    def initialize_database(self):
        """
        Initialize the database by creating the table.
        """
        self.Base.metadata.create_all(self.engine)
        print("Database initialized successfully.")

    def create_model(self):
        """
        Create a model class for the database.
        
        Returns:
            sqlalchemy.ext.declarative.api.DeclarativeMeta: The model class for the database.
        """
        class ApiCall(self.Base):
            __tablename__ = 'api_requests'

            id = Column(Integer, primary_key=True)
            query = Column(String)
            result = Column(Float)

        return ApiCall

    def insert_api_result_in_db(self, query: str, result: float):
        """
        Insert the API result in the SQL table.

        Args:
            query (str): A NPI expression.
            result (float): The result of the expression.
        """
        session = self.Session()
        result_obj = self.model(query=query, result=result)
        session.add(result_obj)
        session.commit()
        session.close()

    def insert_example_data_db(self):
        """
        Insert example data in the SQL table.
        """
        api_results = [
            {'query': '5 3 +', 'result': 8.0},
            {'query': '4 2 * 3 +', 'result': 11.0},
            {'query': '10 2 ÷', 'result': 5.0}
        ]

        for result in api_results:
            self.insert_api_result_in_db(result['query'], result['result'])

    def read_db(self):
        """
        Read all data from the SQL table.

        Returns:
            List: List of all data in the SQL table.
        """
        session = self.Session()
        results = session.query(self.model).all()
        session.close()
        return results

    def remove_all_data_db(self):
        """
        Remove all data from the SQL table.
        """
        session = self.Session()
        session.query(self.model).delete()
        session.commit()
        session.close()
        print("All data removed from the api_requests table.")
