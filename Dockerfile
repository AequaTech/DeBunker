FROM python:3.9
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

WORKDIR /app/API

RUN python initialization4docker.py




CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2000"]