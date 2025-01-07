from models.database import Base, engine
from models.employee import Employee
from models.project import Project
from models.unit import Unit

def create_all_tables():
    Base.metadata.create_all(bind=engine)