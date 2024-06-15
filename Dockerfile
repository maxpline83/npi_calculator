FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt


RUN apt-get update && \
    apt-get install -y curl httpie && \
    rm -rf /var/lib/apt/lists/*

COPY src /app/src
COPY data /app/data

EXPOSE 8000

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "src.api.app:app", "--host", "127.0.0.1", "--port", "8000"]
