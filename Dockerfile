FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

WORKDIR /app/API

RUN python3 initialization4docker.py



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2000"]