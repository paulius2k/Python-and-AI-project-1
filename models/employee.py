from sqlalchemy import Column, Integer, String, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .project_employee import project_employee
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employees'   
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    dob = Column(Date)
    salary = Column(Integer)
    position = Column(String(45))
    employment_dt = Column(Date, server_default=func.now())
    unit_id = Column(Integer, ForeignKey('units.id'), nullable=True)

    projects = relationship('Project', secondary=project_employee, back_populates='employees')
    unit = relationship('Unit', back_populates='employees', foreign_keys='Employee.unit_id')   

    
    def __init__(self, name:str, last_name:str, dob:datetime, salary:int, position:str, **kw):
        super().__init__(**kw)
        self.name = name
        self.last_name = last_name
        self.dob = dob
        self.salary = salary
        self.position = position
        # self.employment_dt = employment_dt
        

    def __str__(self):
        return f"ID {self.id}: {self.name} | {self.last_name} | born: {self.dob} | {self.salary} | {self.position} | employed: {self.employment_dt} | {self.unit.name}"