#!/usr/bin/python3
"""
Contains the class definition of a State and an
instance Base = declarative_base()
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()


class State(Base):
    """
    Defines class State and its attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

Base.metadata.create_all(engine)

session = Session(engine)

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
