from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os 

if os.getenv('FA_ENVIROMENT') != 'prod':
    POSTGRES_USER ='root'
    POSTGRES_PASSWORD = 'root'
    POSTGRES_DB = 'test_db'
    PORT = '5432'
    SERVER = 'localhost'
else:
    POSTGRES_USER ='g6ingsoftware'
    POSTGRES_PASSWORD = 'g6ingsoftware2021'
    POSTGRES_DB = 'g6ingsoftware_bd'
    PORT = '5432'
    SERVER = '146.83.198.35'

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://'+POSTGRES_USER+':'+POSTGRES_PASSWORD+'@'+SERVER+":"+PORT+'/'+POSTGRES_DB
engine = create_engine(SQLALCHEMY_DATABASE_URL
            )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()