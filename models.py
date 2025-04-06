from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Tables = declarative_base()  

class User(Tables):
    __tablename__ = 'Users'  

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100), unique=True)