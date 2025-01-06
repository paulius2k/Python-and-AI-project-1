# 2. Projektų valdymas:
#    - Sukurkite projektų sistemą (pavadinimas, pradžios data, pabaigos data, statusas)
#    - Darbuotojai gali dirbti keliuose projektuose vienu metu (Many-to-Many ryšys)
#    - Galimybė priskirti/pašalinti darbuotojus iš projektų
#    - Galimybė peržiūrėti:
#      * Visus projekto darbuotojus
#      * Visus darbuotojo projektus

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

    def __init__(self, name:str, start_dt:Date, end_dt:Date, status:str, **kw):
        super().__init__(**kw)
        self.name = name
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.status = status
        
    def __str__(self):
        return f"ID {self.id}: {self.name} | {self.start_dt} -- {self.end_dt} | {self.status}"