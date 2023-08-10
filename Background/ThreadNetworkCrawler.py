import sys
sys.path.append('../')
from sqlalchemy import create_engine,or_
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
            links = db.query(Links).filter(
                     or_(Links.source == domain_to_retrieve.domain, Links.timestamp > ten_weeks_ago)).count()

            if links==0: #remove eventually very old links
                db.query(Links).filter(
                 or_(Links.source == domain_to_retrieve.domain, Links.timestamp > ten_weeks_ago)).delete()

                 #fare crawling


if __name__ == "__main__":

    ThreadNetworkCrawler().retrieveDomains()