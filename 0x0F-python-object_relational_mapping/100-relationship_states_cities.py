#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import asc, create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    new_city = City(name='San Francisco', state=new_state)
    session.add(new_city)
    session.commit()

    session.close()
