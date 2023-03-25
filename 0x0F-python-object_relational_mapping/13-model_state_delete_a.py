#!/usr/bin/python3

""" a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for State in states:
        session.delete(State)
    session.commit()
    session.close()
