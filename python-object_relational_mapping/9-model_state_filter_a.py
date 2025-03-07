#!/usr/bin/python3
'''model state filter '''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if name == "main":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for states containing the letter 'a'
    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")
