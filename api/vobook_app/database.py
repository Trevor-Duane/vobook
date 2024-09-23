from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL connection URL using the pymysql driver
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Computers1996.@localhost:3306/vobook"

# Create the engine without check_same_thread since it's for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the declarative models
Base = declarative_base()
