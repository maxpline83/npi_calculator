import pandas as pd
from fastapi import APIRouter
import os

from src.api import get_db_connector

OUTPUT_FILE_PATH = "data/output_files"

router = APIRouter()
db_connector = get_db_connector()


@router.get('/history')
def get_history() -> list:
    results = db_connector.read_db()
    results = [{"query": result.query, "result": result.result} for result in results]
    return results


@router.get('/clear')
def clear_history() -> dict:
    db_connector.remove_all_data_db()
    return {"message": "DB Reset!"}


@router.get('/insert_example_data')
def insert_example_data() -> dict:
    db_connector.insert_example_data_db()
    return {"message": "Example data inserted!"}


@router.get('/export_to_csv/{filename}')
def export_to_csv(filename: str) -> dict:
    results = get_history()
    df = pd.DataFrame(results)
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True)
    df.to_csv(f"{OUTPUT_FILE_PATH}/{filename}", sep=";", index=False)
    return {"message": f"Data exported to {filename}"}
