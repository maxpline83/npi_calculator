import fastapi
from calculator.npi_calculator import eval_npi

app = fastapi.FastAPI()


@app.get("/")
def hello_world():
    return "Hello, World!"

@app.get("/npi_calculator/{expression}")
def compute_expression(expression: str):
    try:
        result = eval_npi(expression)
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"expression": expression, "error": str(e)}
