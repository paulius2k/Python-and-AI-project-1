from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, func, ForeignKey, text
from sqlalchemy.orm import relationship
from models.database import Base
from models.project_employee import project_employee
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employees'   
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    dob = Column(Date)
    salary = Column(Integer)
    position = Column(String(45))
    # employment_dt = Column(TIMESTAMP, server_default=func.now()) 
    unit_id = Column(Integer, ForeignKey('units.id', use_alter=True, name='fk_employee_unit_id'), nullable=True)
    # SQLAlchemy provides the use_alter parameter for foreign key constraints 
    # to delay constraint creation until after both tables are created.
    # Modify one of the relationships to include use_alter=True

    # projects where employee participates
    projects = relationship('Project', secondary=project_employee, back_populates='employees')
    
    # unit where employee works
    unit = relationship('Unit', back_populates='employees', foreign_keys='Employee.unit_id')   
    
    # unit where employee is the head
    managed_dep = relationship('Unit', back_populates='head', foreign_keys='Unit.head_id', uselist=False)
    
    def __init__(self, name:str, last_name:str, dob:datetime, salary:int, position:str, unit_id=None, **kw):
        super().__init__(**kw)
        self.name = name
        self.last_name = last_name
        self.dob = dob
        self.salary = salary
        self.position = position
        self.unit_id = unit_id
        # self.employment_dt = employment_dt
        

    def __str__(self):
        return f"ID {self.id}: {self.name} | {self.last_name} | born: {self.dob} | {self.salary} | {self.position} | employed: {self.employment_dt} | {self.unit.name}"