#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""


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

    objs = session.query(State).filter(State.name.ilike('%a%')).all()
    for obj in objs:
        session.delete(obj)
    session.commit()
    session.close()
