from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base
from .project_employee import project_employee

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    start_dt = Column(Date)
    end_dt = Column(Date)
    status = Column(String(45))
    
    employees = relationship("Employee", secondary=project_employee, back_populates="projects") #Object navigation property

