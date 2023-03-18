#!/usr/bin/python3
"""contains the class definition of a City"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(Base):
    """Defines a city of a state, extends to the Base
    class from sqlalchemy's declartive_base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', backref=backref('cities',
                         cascade='all, delete'))
