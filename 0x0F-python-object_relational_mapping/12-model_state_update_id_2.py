#!/usr/bin/python3
"""cript that changes the name of a State object from the database"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State

    if len(argv) != 4:
        sys.exit('Use:  <mysql.username>'
                 '<mysql passwod><database name>')
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                               '{}'.format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state2 = session.query(State).filter_by(id=2).first()
    if state2 is not None:
        state2.name = 'New Mexico'
    session.commit()
    session.close()
