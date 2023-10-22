#!/usr/bin/python3
"""
Creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)

    session.commit()

    session.close()
