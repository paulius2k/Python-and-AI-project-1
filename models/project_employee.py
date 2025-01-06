from sqlalchemy import Column, Integer, ForeignKey, Table
from .database import Base

project_employee = Table(
            'project_employee', 
            Base.metadata,
            Column('project_id', Integer, ForeignKey('projects.id')),
            Column('employee_id', Integer, ForeignKey('employees.id'))
            )