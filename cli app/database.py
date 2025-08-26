from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Sqlite database - creates a connection
engine = create_engine("sqlite:///order.db", echo=True)

session = sessionmaker(bind=engine)

#Base class for models
Base = declarative_base