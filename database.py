from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./Bank.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)