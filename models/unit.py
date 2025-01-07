from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    head_id = Column(Integer, ForeignKey('employees.id'))           # foreign key į employees LENTELĘ
    location = Column(String(255))
    
    # čia ryšiai nurodomi į KLASĖS foreign key, o ne į LENTELĖS stulpelį
    employees = relationship('Employee', back_populates='unit', foreign_keys="Employee.unit_id")
    head = relationship('Employee', foreign_keys="Unit.head_id")
    
    
    def __init__(self, name:str, location:str, head_id:int=None, **kw):
        super().__init__(**kw)
        self.name = name
        self.head_id = head_id
        self.location = location
    
    def __str__(self):
        if self.head_id:
            head_id_txt = f"{self.head.name} {self.head.last_name}"
        else:
            head_id_txt = self.head_id

        return f"ID {self.id}: {self.name} | head: {head_id_txt} | location: {self.location}"