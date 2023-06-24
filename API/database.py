from sqlalchemy import create_engine
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
    title = Column(Text)
    content = Column(Text)
    date = Column(Date)