from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import config


SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://${PG_USER}:${PG_PASSWORD}@${PG_DOMAIN}:${PG_PORT}/${PG_DB}'

engine = create_engine(config.DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()