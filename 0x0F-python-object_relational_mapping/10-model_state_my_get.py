#!/usr/bin/python3
"""Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db, state_arg = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_arg).first()
    if state is not None:
        print(state.id)
    else:
        print('Not found')
