FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api.app:app", "--host", "127.0.0.1", "--port", "8000"]

