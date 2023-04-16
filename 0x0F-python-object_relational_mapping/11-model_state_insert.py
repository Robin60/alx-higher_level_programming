#!/usr/bin/python3
"""script that adds the State object Louisiana to the database"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State

    if len(argv) != 4:
        sys.exit('Use: 11-model_state_insert.py <mysql.username>'
                 '<mysql passwod><database name>')
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                               '{}'.format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_obj = State(name='Louisiana')
    session.add(new_obj)
    ssession.commit()
    print(new_obj.id)
    session.close()
