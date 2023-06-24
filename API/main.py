import json
from random import randint
from webScraper.WebScraper import WebScraper
import hashlib
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import engine, SessionLocal,Base,Urls
from sqlalchemy.orm import Session
from datetime import datetime
from news_evaluation.danger import Danger

danger = Danger('distilbert-base-uncased', 2)


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
class Url(BaseModel):
    request_id: str = Field(min_Length=1)
    title:      str = Field(min_Length=1)
    content:    str = Field(min_Length=1)
    date:       str = Field(min_length=1)

SQLALCHEMY_DATABASE_URL = "sqlite:///./debunkerAPI.db"


@app.get("/testing")
async def root():
    swap=[]
    lower = 1
    upper = randint(1000,10000)

    print("Prime numbers between", lower, "and", upper, "are:")
    numbers=''
    for num in range(lower, upper + 1):
        swap.append(num)
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numbers+=' '+str(num)
    return {"message": "Prime numbers between"+str(lower)+"and"+str(upper)+"are: "+numbers}


@app.post("/api/v1/scrape")
async def retrieveUrl(url : str, db: Session = Depends(get_db)):
    hash_id = hashlib.md5(url.encode('utf-8')).hexdigest()
    url_object=db.query(Urls).filter(Urls.request_id == hash_id).first()
    if url_object is None:
        webScraper=WebScraper()
        result=webScraper.scrape(url)
        print(result)
        jsonResult=json.loads(result)

        if jsonResult['status_code']==200:
            url_model = Urls()
            url_model.title        = jsonResult['title']
            url_model.content      = '    '#jsonResult['content']
            url_model.date         = datetime.strptime(jsonResult['date'], '%Y-%M-%d')
            url_model.request_id   = hash_id
            db.add(url_model)
            db.commit()
            jsonResult['request_id'] = hash_id

        return jsonResult

    else:

        return {'request_id':url_object.request_id,
                           'status_code':200,
                           'title':url_object.title,
                           'content': url_object.content,
                           'date': datetime.strftime(url_object.date, '%Y-%M-%d')}


@app.get("/api/v1/danger/{request_id}")
async def getDanger(request_id : str, db: Session = Depends(get_db)):
    url_object=db.query(Urls).filter(Urls.request_id == request_id).first()
    if url_object is not None:
        res = danger.stereotype_detection(title=url_object.title)


        return { 'status': 200, 'stereotype': res}

    else:

        return {
                           'status_code':400,
                           'message':'request_id not available. Recover the url content by /api/v1/scrape first.'}