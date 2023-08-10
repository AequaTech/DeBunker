from sqlalchemy import create_engine, BLOB, LargeBinary, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text


SQLALCHEMY_DATABASE_URL = "sqlite:///./debunker.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Urls(Base):
    __tablename__ = "urls"

    request_id = Column(Text, primary_key=True, index=True)
    url = Column(Text)
    title = Column(Text)
    content = Column(Text)
    feat_title = Column(LargeBinary)
    attention_title = Column(LargeBinary)
    feat_content = Column(LargeBinary)
    attention_content = Column(LargeBinary)
    #linguistic_features_title = Column(LargeBinary)
    #linguistic_features_content = Column(LargeBinary)
    date = Column(Date)
    is_reported = Column(Integer,default=0)


class DomainsWhois(Base):
    __tablename__ = "domains_whois"
    domain = Column(Text, primary_key=True, index=True)
    registrant_country = Column(Date,default=None)
    creation_date = Column(Date,default=None)
    expiration_date = Column(Date,default=None)
    last_updated = Column(Date,default=None)

class DomainsNetworkMetrics(Base):
    __tablename__ = "domains_network_metrics"
    domain = Column(Text, primary_key=True, index=True)
    pagerank=Column(Float,default=None)
    closeness=Column(Float,default=None)
    betweenness=Column(Float,default=None)
    hub=Column(Float,default=None)
    authority = Column(Float,default=None)
    degree_in = Column(Integer,default=None)
    degree_out = Column(Integer,default=None)
    neighborhood_list= Column(Text,default=None)
    white_community = Column(Float,default=None)
    black_community = Column(Float,default=None)
    white_list= Column(Text,default=None)
    black_list= Column(Text,default=None)


class Links(Base):
    __tablename__ = "links"

    source = Column(Text, primary_key=True, index=True)
    target = Column(Text, primary_key=True, index=True)
    weight = Column(Integer)
