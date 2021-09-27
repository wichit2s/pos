from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core import config

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@172.29.0.2:5432/postgres'
engine = create_engine(
    #config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_DATABASE_URI,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
