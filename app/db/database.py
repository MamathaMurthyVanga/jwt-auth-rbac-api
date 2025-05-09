# # app/db/database.py

from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    print(" App startup: creating tables...")
    SQLModel.metadata.create_all(engine)

# Add this function to provide session dependency
def get_session():
    with Session(engine) as session:
        yield session
