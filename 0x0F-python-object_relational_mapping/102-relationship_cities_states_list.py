#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

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

    for city in session.query(City).order_by(City.id).all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    session.close()
