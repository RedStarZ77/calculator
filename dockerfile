FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt

EXPOSE 3001

CMD ["python", "main.py"]
