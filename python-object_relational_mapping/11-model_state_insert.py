#!/usr/bin/python3
""" module contains the function model_state_insert() """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_insert():

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    engine_ = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine_)
    State.metadata.create_all(engine_)

    Session = sessionmaker(bind=engine_)

    conn = engine_.connect()
    session = Session(bind=conn)

    _new_state = State(name='louisiana')
    session.add(_new_state)
    session.commit()
    print(_new_state.id)


if __name__ == "__main__":
    model_state_insert
