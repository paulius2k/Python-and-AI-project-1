from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    
    employee_id = Column(Integer, ForeignKey('employees.id'))       # lentelių surišimas
    
    employee = relationship('Employee', back_populates='tasks')     # klasių surišimas: "ištrauk darbuotoją su visomis jo užduotimis"
                                                                    # object navigation property
                                                                    