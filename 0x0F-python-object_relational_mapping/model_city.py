#!/usr/bin/python3
"""contains the class definition of a State and an instance
   Base = declarative_base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Defines the City class to be mapped to cities state
    __tablename__ (str): The database table to be maped to
    id (Integer): The city's id.
    name(String): The city's name.
    state_id(String): Foreign key of state's id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeinKey("states.id"), nullable=False)
