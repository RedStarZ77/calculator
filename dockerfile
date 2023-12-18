FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY * /app

RUN pip install flask flask_cors asyncio requests

EXPOSE 3001

CMD ["python", "main.py"]
