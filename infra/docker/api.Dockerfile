FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --retries 20 --timeout 1000 -r requirements.txt

COPY . .

CMD ["uvicorn", "services.api_service.main:app", "--host", "0.0.0.0", "--port", "8000"]