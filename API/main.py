import json
import random

import numpy
from sqlalchemy.exc import IntegrityError

from news_evaluation.sensationalism import Sensationalism
from PreProcessing.PreProcessing import BertBasedTokenizer
from webScraper.WebScraper import WebScraper
import hashlib
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import engine, SessionLocal,Base,Urls,DomainsWhois, DomainsNetworkMetrics
from sqlalchemy.orm import Session
from datetime import datetime
from news_evaluation.danger import Danger
import tldextract

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
            url_model.url          = url
            url_model.title        = jsonResult['result']['title']
            url_model.content      = jsonResult['result']['content']
            url_model.date         = datetime.strptime(jsonResult['result']['date'], '%Y-%M-%d')
            url_model.feat_title,    url_model.attention_title   = tokenizer_bert.tokenize_text(url_model.title)
            url_model.feat_content,  url_model.attention_content = tokenizer_bert.tokenize_text(url_model.content)
            url_model.request_id   = hash_id
            db.add(url_model)
            db.commit()
            jsonResult['result']['request_id'] = hash_id

            domains_whois_model = DomainsWhois()
            domains_whois_model.domain=tldextract.extract(url).domain
            db.add(domains_whois_model)
            db.commit()

            domains_network_metrics = DomainsNetworkMetrics()
            domains_network_metrics.domain=tldextract.extract(url).domain
            db.add(domains_network_metrics)
            db.commit()

        return  jsonResult


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



@app.post("/api/v1/report_domain")
async def getReportDomain(url : str, db: Session = Depends(get_db)):
    webScraper = WebScraper()
    result = webScraper.scrape(url)
    jsonResult = json.loads(result)

    if jsonResult['status_code'] == 200:

        try:

            domains_whois_model = DomainsWhois()
            domains_whois_model.domain = tldextract.extract(url).domain
            db.add(domains_whois_model)
            db.commit()

            domains_network_metrics = DomainsNetworkMetrics()
            domains_network_metrics.domain = tldextract.extract(url).domain
            db.add(domains_network_metrics)
            db.commit()

            return { 'status': 200, 'message': 'domain has been successfully reported'}
        except IntegrityError:
            return { 'status': 200, 'message': 'domain had already been reported'}
    else:
        return {'status': 400, 'message': 'the domain is not available or does not exist'}


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
        colloquial= sensationalism.get_clickbait_style(url_object)

        return { 'status': 200,
                 'message': 'the request was successful',
                 'result': { 'overall': numpy.average([informal_style['overall'], sentiment_affective['overall'],readability['overall'],colloquial['overall'] ]),
                             'informal_style' :informal_style,
                             'sentiment_affective' :sentiment_affective,
                             'readability':readability,
                             'clickbait_style': colloquial,

                 }}
    else:

        return {'status_code':400,'message':'request_id not available. Recover the content of the url by /api/v1/scrape first.'}


@app.get("/api/v1/echo_effect/{request_id}")
async def getEchoEffect(request_id : str, db: Session = Depends(get_db)):

    return { 'status': 200,
             'message': 'the request was successful (random values)',
             'result': { 'overall': random.random(),
                         'pagerank' : random.random(),
                         'closeness' : random.random(),
                         'betweenness' : random.random(),
                         'hub' : random.random(),
                         'authority' : random.random(),
             }}


@app.get("/api/v1/reliability/{request_id}")
async def getReliability(request_id : str, db: Session = Depends(get_db)):

    return { 'status': 200,
             'message': 'the request was successful (random values)',
             'result': {
                         'overall': random.random(),
                         'whitelist': {
                                         'sources': ['domain1','domain2'],
                                         'info': 'information about the sources from with we recover the whitelist'
                                      },
                         'blacklist': {
                             'sources': ['domain3', 'domain4'],
                             'info': 'information about the sources from with we recover the whitelist'
                         },

                         'neighborhood': {
                            'degree_in': random.randint(1,100),
                            'degree_out': random.randint(1,100),
                            'neighborhood_list': [('domain1', random.randint(1,100)),('domain2', random.randint(1,100)),('domain3', random.randint(1,100)),('domain4', random.randint(1,100)),('domain5', random.randint(1,100))],
                            'black_community': random.random(),
                            'white_community': random.random(),
                         },

                         'solidity': {
                               'overall': random.random(),
                               'registrant_country': 'IT',
                               'creation_date': '2005/01/01',
                               'expiration_date': '2025/01/01',
                               'last_updated': '2003/01/01'
                         }
                    }
             }
