#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if first_state is not None:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')
