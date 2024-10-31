from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base # Used to make models

# Database connection details
# postgresql_db_url = "postgresql+psycopg2://<username>:<password>@<hostname>:<port>/<database>"
postgresql_db_url = "postgresql+psycopg2://postgres:1234@localhost:5432/learn_sqlalchemy"

engine = create_engine(postgresql_db_url)

Base = declarative_base()

#create a table
class User(Base):
    __tablename__ = "users" # Table name in database
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


Base.metadata.create_all(engine)
