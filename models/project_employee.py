from sqlalchemy import Column, Integer, ForeignKey, Table
from models.database import Base

project_employee = Table(
            'project_employee', 
            Base.metadata,
            Column('project_id', Integer, ForeignKey('projects.id')),
            Column('employee_id', Integer, ForeignKey('employees.id'))
            )



# This is a collection of all table and relationship definitions associated with the Base declarative base.
# When you create tables using Base.metadata.create_all(), 
# SQLAlchemy looks for all table definitions tied to the Base's metadata.

# Association Table:
# Since the project_employee table is explicitly added to Base.metadata during its definition, 
# it is included in the table creation process.