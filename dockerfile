FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY . .



RUN pip install flask flask_cors

CMD ["python", "main.py"]

