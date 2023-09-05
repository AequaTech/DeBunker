FROM python:3.9
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt
WORKDIR /app/API

RUN python news_evaluation/danger.py

CMD ["uvicorn", "--port", "2000","main:app"]
