from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)