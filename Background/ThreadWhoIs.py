import sys
sys.path.append('../')
from sqlalchemy import create_engine,or_
from sqlalchemy.orm import sessionmaker
from API.database import Links,Base,Urls,DomainsWhois
import requests
import datetime
import whois
import time


class ThreadWhoIs:
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
        domains_to_retrieve=db.query(DomainsWhois).filter(or_(DomainsWhois.overall == None,DomainsWhois.timestamp<ten_weeks_ago))
        #@urbinati, ragionare meglio l'overall sul parametro solidity
        for domain_to_retrieve in domains_to_retrieve:
            try:
                time.sleep(2)
                w = whois.query(domain_to_retrieve.domain)
                domain_to_retrieve.registrant_country=w.registrant_country
                domain_to_retrieve.creation_date=w.creation_date
                domain_to_retrieve.expiration_date=w.expiration_date
                domain_to_retrieve.last_updated=w.last_updated
                overall=0
                five_years_ago = current_time - datetime.timedelta(weeks=53*5)
                if current_time-domain_to_retrieve.creation_date>=current_time-five_years_ago:
                    overall+=0.5
                one_year_ago = current_time - datetime.timedelta(days=356)
                if current_time-domain_to_retrieve.last_updated<current_time-one_year_ago:
                    overall+=0.5
                domain_to_retrieve.overall=overall


                db.commit()
            except:
                continue

if __name__ == "__main__":

    ThreadWhoIs().retrieveDomains()