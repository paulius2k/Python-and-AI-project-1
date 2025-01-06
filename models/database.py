from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import my_secrets as secrets


db_connect_string = f'mysql://paulius:{secrets.MY_SQL_PSSW}@localhost/testine_db'
engine = create_engine(db_connect_string)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)

def get_session():
    return Session()