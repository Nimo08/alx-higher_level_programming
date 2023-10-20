#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
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
