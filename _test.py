from sqlalchemy.sql import select
from models.database import get_session
import modules.employee_functions as ef
from models.employee import Employee
from models.project import Project
from models.unit import Unit

session = get_session()

# person = (
#     "Vardas",
#     "Pavarde",
#     "1990-01-01",
#     1000,
#     "Developer"
# )
# # new_person = Employee(name=person[0], last_name=person[1], dob=person[2], salary=person[3], position=person[4])

# ef.create_employee(person, db)

with session:
    # query2 = select(Project).where(Project.employees.id < 10000)
    query2 = select(Project).where(Project.employees.any(Employee.id < 10000))
    all_projects = session.scalars(query2)
    for project in all_projects:
            print(f"     {project}")

