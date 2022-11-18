#!/usr/bin/python3
""" module contains the function model_state_fetch_all() """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_all():
    """ lists all state objects from database hbtn_0e_6_usa """

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine_ = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine_)
    State.metadata.create_all(engine_)

    Session = sessionmaker(bind=engine_)

    conn = engine_.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        print('{}: {}'.format(obj.id, obj.name))


if __name__ == "__main__":
    model_state_fetch_all()
