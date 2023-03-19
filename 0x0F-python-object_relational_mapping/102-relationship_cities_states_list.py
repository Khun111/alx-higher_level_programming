#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost\
:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City)
    for city in query.all():
        print(f'{city.id}: {city.name} -> {city.state.name}')
    session.close()
