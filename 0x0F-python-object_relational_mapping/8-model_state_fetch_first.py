#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State, session
from sqlalchemy import create_engine


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    empty_state = session.query(State).count() == 0
    if empty_state:
        print("Nothing")
    state = session.query(State).filter(State.id == 1).first()
    if state:
        print(f"{state.id}: {state.name}")
