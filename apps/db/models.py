from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

# # postgresql
# DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/graphql_test"

# engine = create_engine(DATABASE_URL, echo=True)

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    email: str = Field(default=None)
    created_at: datetime = Field(default=datetime.now(), primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.now(), primary_key=True)

    class Config:
        orm_mode = True

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# if __name__ == '__main__':
#     create_db_and_tables()