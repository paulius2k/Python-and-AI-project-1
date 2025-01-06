from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    head_id = Column(Integer, ForeignKey('employees.id'))
    location = Column(String(255))
    
    employees = relationship('Employee', back_populates='unit', foreign_keys="Employee.unit_id")
    