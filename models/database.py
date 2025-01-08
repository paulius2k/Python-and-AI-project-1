from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import my_secrets as secrets
# from sqlalchemy.ext.declarative import declarative_base
# from models.database import Base, engine
# from models.employee import Employee
# from models.project import Project
# from models.unit import Unit

class Base(DeclarativeBase):
    pass

# Base = declarative_base()

db_connect_string = f'mysql://paulius:{secrets.MY_SQL_PSSW}@localhost/employee_db'
engine = create_engine(db_connect_string)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()