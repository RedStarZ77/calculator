FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY . .



RUN pip install flask flask_cors asyncio requests

CMD ["python", "main.py"]
