from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseConnector:
    def __init__(self):
        self.engine = create_engine('sqlite:///data/database/api_requests.db', echo=True)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.model = self.create_model()
        print("Database connected successfully.")

    def initialize_database(self):
        self.Base.metadata.create_all(self.engine)
        print("Database initialized successfully.")

    def create_model(self):
        class ApiCall(self.Base):
            __tablename__ = 'api_requests'

            id = Column(Integer, primary_key=True)
            query = Column(String)
            result = Column(Float)

        return ApiCall

    def insert_api_result(self, query: str, result: float):
        session = self.Session()
        result_obj = self.model(query=query, result=result)
        session.add(result_obj)
        session.commit()
        session.close()

    def insert_example_data(self):
        api_results = [
            {'query': '5 3 +', 'result': 8.0},
            {'query': '4 2 * 3 +', 'result': 11.0},
            {'query': '10 2 ÷', 'result': 5.0}
        ]

        for result in api_results:
            self.insert_api_result(result['query'], result['result'])

    def read_db(self):
        session = self.Session()
        results = session.query(self.model).all()
        session.close()
        return results

    def remove_all_data(self):
        session = self.Session()
        session.query(self.model).delete()
        session.commit()
        session.close()
        print("All data removed from the api_requests table.")
