#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import asc, create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(asc(City.id)).all()
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
    session.close()
