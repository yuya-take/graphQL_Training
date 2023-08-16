import os
import sys

from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Session, select

sys.path.append("..")   
from db.models import User

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/graphql_test"
engine = create_engine(DATABASE_URL, echo=True)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post('/user/')
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.get('/user/')
def get_user():
    with Session(engine) as session:
        heroes = session.exec(select(User)).all()
        return heroes