#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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

    query = session.query(State, City).filter(State.id == City.state_id)
    res = query.order_by(State.id, City.id).all()
    cur_state = None
    for state, city in res:
        if state.id != cur_state:
            cur_state = state.id
            print(f"{state.id}: {state.name}")
        print(f"    {city.id}: {city.name}")
    session.close()
