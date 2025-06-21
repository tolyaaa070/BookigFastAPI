from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine



DB_URL = 'postgresql://postgres:admin@localhost/booking'

first = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=first)

Base = declarative_base()