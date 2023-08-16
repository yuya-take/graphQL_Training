import os

from sqlmodel import create_engine

from models import *

# postgresql
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/graphql_test"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)
