import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# URL.create safely handles special characters in the MySQL password.
DATABASE_URL = URL.create(
    drivername="mysql+mysqlconnector",
    username=os.getenv("test", "test"),
    password=os.getenv("DB_PASSWORD", "Kousalya@1125"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME", "product_store"),
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
