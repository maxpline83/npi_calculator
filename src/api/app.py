from fastapi import FastAPI
from src.calculator.npi_calculator import eval_npi
from src.database.database import DatabaseConnector
import pandas as pd

output_file_path = "data/output_files"

db_connector = DatabaseConnector()
db_connector.initialize_database()

app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello, World!"


@app.get("/npi_calculator/{expression}")
def compute_expression(expression: str):
    try:
        result = eval_npi(expression)
        db_connector.insert_api_result(expression, result)
        return {"expression": expression, "result": result}
    except Exception as e:
        # TODO: insert error in database
        return {"expression": expression, "error": str(e)}


@app.get('/history')
def get_history():
    results = db_connector.read_db()
    results = [{"query": result.query, "result": result.result} for result in results]
    return results


@app.get('/clear')
def clear_history():
    db_connector.remove_all_data()
    return {"message": "History cleared!"}


@app.get('/insert_example_data')
def insert_example_data():
    db_connector.insert_example_data()
    return {"message": "Example data inserted!"}


@app.get('/export_to_csv/{filename}')
def export_to_csv(filename: str):
    results = get_history()
    df = pd.DataFrame(results)
    df.to_csv(f"{output_file_path}/{filename}", sep=";", index=False)
    return {"message": f"Data exported to {filename}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
