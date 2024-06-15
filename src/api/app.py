from fastapi import FastAPI

from src.api.routers import calculator, database

app = FastAPI()


@app.get("/")
def hello_world() -> str:
    return "Hello, World!"


app.include_router(calculator.router, prefix="/calculator", tags=["calculator"])
app.include_router(database.router, prefix="/database", tags=["database"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
