from fastapi import APIRouter

from src.api import get_db_connector
from src.calculator.npi_calculator import eval_npi

router = APIRouter()
db_connector = get_db_connector()


@router.get("/npi_calculator/{expression}")
def compute_expression(expression: str) -> dict:
    try:
        result = eval_npi(expression)
        db_connector.insert_api_result_in_db(expression, result)
        return {"expression": expression, "result": result}
    except Exception as e:
        # TODO: insert error in database
        return {"expression": expression, "error": str(e)}
