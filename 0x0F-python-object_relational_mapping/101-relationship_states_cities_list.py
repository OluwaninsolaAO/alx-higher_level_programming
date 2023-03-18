#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import asc, create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))
        i = 0
        while i < len(state.cities):
            print('    {}: {}'.format(state.cities[i].id,
                                      state.cities[i].name))
            i += 1

    session.close()
