import json
import random
import time
from urllib.parse import urlparse

import numpy
from sqlalchemy.exc import IntegrityError

from PreProcessing.PreProcessing import PreprocessingSpacy
from news_evaluation.sensationalism import Sensationalism
from PreProcessing.PreProcessing import BertBasedTokenizer
from webScraper.WebScraper import WebScraper
import hashlib
from fastapi import FastAPI, Depends
from database import engine, SessionLocal,Base,Urls,DomainsWhois, DomainsNetworkMetrics, getdb
from sqlalchemy.orm import Session
from datetime import datetime, time,timedelta
from news_evaluation.danger import Danger
#import tldextract

from Background.ThreadNetworkCrawler import ThreadNetworkCrawler
from Background.ThreadNetworkMetrics import ThreadNetworkMetrics
from Background.ThreadWhoIs import ThreadWhoIs
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware


"""from fastapi_utils.tasks import repeat_every"""

danger = Danger('dbmdz/bert-base-italian-cased', 2)
sensationalism = Sensationalism()


tokenizer_bert = BertBasedTokenizer('dbmdz/bert-base-italian-cased')

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)





preprocessing_spacy=PreprocessingSpacy('it')






@app.post("/api/v1/scrape")
async def retrieveUrl(url : str, db: Session = Depends(get_db)):
    hash_id = hashlib.md5(url.encode('utf-8')).hexdigest()
    url_object=db.query(Urls).filter(Urls.request_id == hash_id).first()
    if url_object is None:
        webScraper=WebScraper()
        result=webScraper.scrape(url)
        jsonResult=json.loads(result)

        if jsonResult['status'] == 200:
            url_model = Urls()
            url_model.url          = url
            url_model.title        = jsonResult['result']['title']
            url_model.content  = jsonResult['result']['content'].replace('\n',' ')
            url_model.date         = datetime.strptime(jsonResult['result']['date'], '%Y-%M-%d')
            url_model.feat_title,    url_model.attention_title   = tokenizer_bert.tokenize_text(url_model.title)
            url_model.feat_content,  url_model.attention_content = tokenizer_bert.tokenize_text(url_model.content)
            #url_model.linguistic_features_title = preprocessing_spacy.get_linguistic_features_from_text(url_model.title)
            #url_model.linguistic_features_content = preprocessing_spacy.get_linguistic_features_from_text(url_model.content)
            url_model.request_id   = hash_id
            db.add(url_model)
            db.commit()
            jsonResult['result']['request_id'] = hash_id

            #result=db.query(DomainsWhois).filter(DomainsWhois.domain==tldextract.extract(url).registered_domain).first()
            result=db.query(DomainsWhois).filter(DomainsWhois.domain==urlparse(url).netloc).first()
            if result is None:
                domains_whois_model = DomainsWhois()
                domains_whois_model.domain=urlparse(url).netloc#tldextract.extract(url).registered_domain
                db.add(domains_whois_model)
                db.commit()
            #result=db.query(DomainsNetworkMetrics).filter(DomainsNetworkMetrics.domain==tldextract.extract(url).registered_domain).first()
            result=db.query(DomainsNetworkMetrics).filter(DomainsNetworkMetrics.domain==urlparse(url).netloc).first()
            if result is None:
                domains_network_metrics = DomainsNetworkMetrics()
                domains_network_metrics.domain=urlparse(url).netloc#tldextract.extract(url).registered_domain
                db.add(domains_network_metrics)
                db.commit()

        return  jsonResult


    else:

        return {'status':200,
                'message':'the request was successful',
                'result': {
                        'request_id':url_object.request_id,
                        'status':200,
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

    if jsonResult['status'] == 200:

        try:

            domains_whois_model = DomainsWhois()
            domains_whois_model.domain = urlparse(url).netloc#tldextract.extract(url).registered_domain
            db.add(domains_whois_model)
            db.commit()

            domains_network_metrics = DomainsNetworkMetrics()
            domains_network_metrics.domain = urlparse(url).netloc#tldextract.extract(url).registered_domain
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

        return {'status':400,'message':'request_id not available. Recover the content of the url by /api/v1/scrape first.'}


@app.get("/api/v1/sensationalism/{request_id}")
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

        return {'status':400,'message':'request_id not available. Recover the content of the url by /api/v1/scrape first.'}


@app.get("/api/v1/echo_effect/{request_id}")
async def getEchoEffect(request_id : str, db: Session = Depends(get_db)):
    url_object = db.query(Urls).filter(Urls.request_id == request_id).first()
    domain = urlparse(url_object.url).netloc#tldextract.extract(url_object.url).registered_domain


    domains_network_metrics_object = db.query(DomainsNetworkMetrics).filter(DomainsNetworkMetrics.domain == domain).first()

    if domains_network_metrics_object is None or domains_network_metrics_object.pagerank is None:
        return {'status': 200,
                'message': 'the request was successful, but there is currently no information about the domain but the request has been registered, try again in a day' }
    else:
        return { 'status': 200,
                 'message': 'the request was successful',
                 'result': { 'overall': domains_network_metrics_object.authority*domains_network_metrics_object.betweenness,
                             'pagerank' : domains_network_metrics_object.pagerank,
                             'closeness' : domains_network_metrics_object.closeness,
                             'betweenness' : domains_network_metrics_object.betweenness,#[0,---]
                             'hub' : domains_network_metrics_object.hub,
                             'authority' : domains_network_metrics_object.authority, #[0,1]
                 }}




@app.get("/api/v1/reliability/{request_id}")
async def getReliability(request_id : str, db: Session = Depends(get_db)):
    url_object = db.query(Urls).filter(Urls.request_id == request_id).first()
    domain = urlparse(url_object.url).netloc#tldextract.extract(url_object.url).registered_domain

    domains_whois_object = db.query(DomainsWhois).filter(DomainsWhois.domain == domain).first()


    domains_network_metrics_object = db.query(DomainsNetworkMetrics).filter(DomainsNetworkMetrics.domain == domain).first()


    if domains_network_metrics_object is None or domains_network_metrics_object.pagerank is None:
        return {'status': 200,
                'message': 'the request was successful, but there is currently no information about the domain but the request has been registered, try again in a day' }
    else:
        return { 'status': 200,
                 'message': 'the request was successful (random values)',
                 'result': {
                             'whitelist': json.loads(domains_network_metrics_object.white_list),
                             'blacklist': json.loads(domains_network_metrics_object.black_list),
                             'in_blacklist': domains_network_metrics_object.is_blacklist,
                             'neighborhood': {
                                 'overall': domains_network_metrics_object.white_community/(domains_network_metrics_object.white_community+domains_network_metrics_object.black_community) if (domains_network_metrics_object.white_community+domains_network_metrics_object.black_community)>0 else 0,
                                 # @urbinati, da decidere. Se è in black list metterei 0, altrimenti, metterei
                                 # white_community/(white_community+black_community)
                                'degree_in': domains_network_metrics_object.degree_in,
                                'degree_out': domains_network_metrics_object.degree_out,
                                'neighborhood_list': json.loads(domains_network_metrics_object.neighborhood_list), #[('domain1', random.randint(1,100)),('domain2', random.randint(1,100)),('domain3', random.randint(1,100)),('domain4', random.randint(1,100)),('domain5', random.randint(1,100))],
                                'black_community': domains_network_metrics_object.black_community,
                                'white_community': domains_network_metrics_object.white_community,
                             },

                             'solidity': {
                                   'overall': domains_whois_object.overall,
                                   'registrant_country': domains_whois_object.registrant_country,
                                   'creation_date': domains_whois_object.creation_date,
                                   'expiration_date': domains_whois_object.expiration_date,
                                   'last_updated': domains_whois_object.expiration_date
                             }
                        }
                 }





scheduler=BackgroundScheduler()
def NetworkCrawler():
    print("Starting background processes")

    ThreadNetworkCrawler().retrieveDomains()

    ThreadWhoIs().retrieveDomains()

    ThreadNetworkMetrics().retrieveDomains()




tomorrow_start = datetime.combine(datetime.today(), time(0, 0)) + timedelta(1)

#scheduler.add_job(NetworkCrawler, 'interval', hours=24,max_instances=1,next_run_time=tomorrow_start)
scheduler.add_job(NetworkCrawler, 'interval', minutes=5,max_instances=1)#,next_run_time=tomorrow_start)
scheduler.start()