#!/usr/bin/python3
"""Contains the class definition of a State and an
instance Base = declarative_base()"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class representing a state, with each instances
    with its own unique id and name."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
