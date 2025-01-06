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
    
    def __init__(self, name:str, location:str, head_id:int=None, **kw):
        super().__init__(**kw)
        self.name = name
        self.head_id = head_id
        self.location = location
    
    def __str__(self):
        return f"ID {self.id}: {self.name} | {self.head_id} | {self.location}"