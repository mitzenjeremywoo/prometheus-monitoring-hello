# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY main.py .

RUN pip install flask prometheus_client

EXPOSE 8000

CMD ["python", "app.py"]
