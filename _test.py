from models.database import get_session
import modules.employee_functions as ef

db = get_session()

person = (
    "Vardas",
    "Pavarde",
    "1990-01-01",
    1000,
    "Developer"
)
# new_person = Employee(name=person[0], last_name=person[1], dob=person[2], salary=person[3], position=person[4])

ef.create_employee(person, db)