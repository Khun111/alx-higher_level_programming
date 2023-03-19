#!/usr/bin/python3
''' Module for abstracting State class to state table '''
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    '''State Class to abstract to states'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(City, cascade='all, delete', backref='state')
