#!/usr/bin/python3
"""
Contains the class definition of a State and an
instance Base = declarative_base()
"""


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
                       .format("nimo", "House27809!", "hbtn_0e_6_usa"),
                       pool_pre_ping=True)

Base.metadata.create_all(engine)

session = Session(engine)

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(states.id, states.name))
session.close()
