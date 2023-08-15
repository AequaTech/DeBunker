import sys

from Background.WebCrawler import WebCrawler

sys.path.append('../')
from sqlalchemy import create_engine,or_,and_
from sqlalchemy.orm import sessionmaker
from API.database import Links,Base,Urls,DomainsWhois,DomainsNetworkMetrics
import requests
import datetime
import whois
import time


class ThreadNetworkCrawler:
    @staticmethod
    def retrieveDomains():
        SQLALCHEMY_DATABASE_URL = "sqlite:///../API/debunker.db"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)

        db = SessionLocal()
        current_time = datetime.datetime.utcnow()

        ten_weeks_ago = current_time - datetime.timedelta(weeks=10)
        domains_to_retrieve=db.query(DomainsNetworkMetrics).filter(or_(DomainsNetworkMetrics.overall == None,DomainsNetworkMetrics.timestamp<ten_weeks_ago))

        for domain_to_retrieve in domains_to_retrieve:
            #remove eventually very old links
            db.query(Links).filter(
             and_(Links.source == domain_to_retrieve.domain, Links.timestamp < ten_weeks_ago)).delete()

            edges=WebCrawler.retrieveDomains('http://'+domain_to_retrieve.domain,domain_to_retrieve.domain) #protocollo per il primo parametro?

            #insert edges in db
            for edge in edges:
                link_model = Links()
                link_model.source=edge[0]
                link_model.target=edge[1]
                link_model.weight=edge[2]
                db.add(link_model)
                db.commit()

if __name__ == "__main__":

    ThreadNetworkCrawler().retrieveDomains()