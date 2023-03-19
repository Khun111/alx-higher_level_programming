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

    astate = State(name='California')
    acity = City(name='San Francisco', state=astate)
    session.add_all([astate, acity])
    session.commit()
    session.close()
