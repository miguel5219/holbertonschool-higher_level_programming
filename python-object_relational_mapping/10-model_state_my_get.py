#!/usr/bin/python3
""" module contains the  function model_state_my_get() """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def model_state_my_get():
    """ prints the state object with the named passed as
    argument from the database """

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    if ';' in sys.argv[4]:
        return

    engine_ = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine_)
    State.metadata.create_all(engine_)

    Session = sessionmaker(bind=engine_)

    conn = engine_.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        if sys.argv[4] == obj.name:
            print(obj.id)
            return
    print('Not found')


if __name__ == "__main__":
    model_state_my_get()