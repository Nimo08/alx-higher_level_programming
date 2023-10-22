#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(City).join(State)\
        .order_by(City.id).all()
    for city in query:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
