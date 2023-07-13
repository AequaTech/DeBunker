import json
from random import randint

import numpy
from news_evaluation.sensationalism import Sensationalism
from PreProcessing.PreProcessing import BertBasedTokenizer
from webScraper.WebScraper import WebScraper
import hashlib
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import engine, SessionLocal,Base,Urls
from sqlalchemy.orm import Session
from datetime import datetime
from news_evaluation.danger import Danger
from aequaTech_packages.analysis import affective_analyses

danger = Danger('dbmdz/bert-base-italian-cased', 2)
sensationalism = Sensationalism()


tokenizer_bert = BertBasedTokenizer('dbmdz/bert-base-italian-cased')

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
class Url(BaseModel):
    request_id       :  str    = Field(min_Length=1)
    title            :  str    = Field(min_Length=1)
    content          :  str    = Field(min_Length=1)
    feat_title       :  object = Field(min_Length=1)
    attention_title  :  object = Field(min_Length=1)
    feat_content     :  object = Field(min_Length=1)
    attention_content:  object = Field(min_Length=1)
    date             :  str    = Field(min_length=1)

SQLALCHEMY_DATABASE_URL = "sqlite:///./debunkerAPI.db"


@app.post("/api/v1/scrape")
async def retrieveUrl(url : str, db: Session = Depends(get_db)):
    hash_id = hashlib.md5(url.encode('utf-8')).hexdigest()
    url_object=db.query(Urls).filter(Urls.request_id == hash_id).first()
    if url_object is None:
        webScraper=WebScraper()
        result=webScraper.scrape(url)
        print(result)
        jsonResult=json.loads(result)

        if jsonResult['status_code'] == 200:
            url_model = Urls()
            url_model.title        = jsonResult['title']
            url_model.content      = jsonResult['content']
            url_model.date         = datetime.strptime(jsonResult['date'], '%Y-%M-%d')
            url_model.feat_title,    url_model.attention_title   = tokenizer_bert.tokenize_text(url_model.title)
            url_model.feat_content,  url_model.attention_content = tokenizer_bert.tokenize_text(url_model.content)
            url_model.request_id   = hash_id
            db.add(url_model)
            db.commit()
            jsonResult['request_id'] = hash_id

        return jsonResult

    else:

        return {'status':200,
                'message':'the request was successful',
                'result': {
                        'request_id':url_object.request_id,
                        'status_code':200,
                        'title':url_object.title,
                        'content': url_object.content,
                        'date': datetime.strftime(url_object.date, '%Y-%M-%d'),
                        'is_reported':url_object.is_reported
                        }
                }



@app.get("/api/v1/report_url/{request_id}")
async def getReportUrl(request_id : str, db: Session = Depends(get_db)):
    url_object=db.query(Urls).filter(Urls.request_id == request_id).first()

    if url_object is not None:
        url_object.is_reported=1
        db.commit()


        return { 'status': 200, 'message': 'url has been successfully reported'}
    else:
        return { 'status': 400, 'message': 'request_id unavailable'}




@app.get("/api/v1/danger/{request_id}")
async def getDanger(request_id : str, db: Session = Depends(get_db)):
    url_object=db.query(Urls).filter(Urls.request_id == request_id).first()
    if url_object is not None:

        res = danger.prediction(url_object)

        return { 'status': 200, 'message':'the request was successful', 'result': res  }

    else:

        return {'status_code':400,'message':'request_id not available. Recover the content of the url by /api/v1/scrape first.'}



@app.get("/api/v1/sentiationalism/{request_id}")
async def getSentiationalism(request_id : str, db: Session = Depends(get_db)):
    url_object=db.query(Urls).filter(Urls.request_id == request_id).first()
    if url_object is not None:

        informal_style = sensationalism.informal_style(url_object)
        sentiment_affective = sensationalism.get_affective_analysis(url_object)
        readability = sensationalism.get_readability_scores(url_object)
        colloquial= sensationalism.get_colloquial_style(url_object)

        return { 'status': 200,
                 'message': 'the request was successful',
                 'result': { 'overall': numpy.average([informal_style['overall'], sentiment_affective['overall'],readability['overall'],colloquial['overall'] ]),
                             'informal_style' :informal_style,
                             'sentiment_affective' :sentiment_affective,
                             'readability':readability,
                             'colloquial': colloquial,

                 }}
    else:

        return {'status_code':400,'message':'request_id not available. Recover the content of the url by /api/v1/scrape first.'}

