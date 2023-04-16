#!/usr/bin/python3
"""that prints all City objects from the database hbtn_0e_14_usa"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State
    from model_city import City

    if len(argv) != 4:
        sys.exit('Use: 14-model_city_fetch_by_state.py <mysql.username>'
                 '<mysql passwod><database name>')
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                               '{}'.format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id).all()
    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))

    session.close()
