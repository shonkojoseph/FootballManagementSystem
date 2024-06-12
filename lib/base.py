from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///football_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_all():
    Base.metadata.create_all(engine)
