from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select, update
from models.employee import Employee
from models.database import get_session
from modules.utilities import date_input


def get_input_for_employee():
    try:
        name = input("Enter employee name: ")
        last_name = input("Enter employee last name: ")
        dob = date_input("Enter date of birth (YYYY-MM-DD): ", allow_future=False)
        salary = input("Enter salary: ")
        if salary in [None, '']:
            salary = None
        else:
            salary = int(salary)
        
        position = input("Enter employee position: ")
        unit_id = input("Enter employee's unit ID (press enter if not known): ")
        if unit_id in [None, '']:
            unit_id = None
    except Exception as err:       
        print("Invalid input")
        return None
    return name, last_name, dob, salary, position, unit_id

def create_employee(person, session):
    try:
        if person:
            new_person = Employee(name=person[0], last_name=person[1], dob=person[2], salary=person[3], position=person[4], unit_id=person[5])
            with session:
                session.add(new_person)
                session.commit()
        
        print("Employee added")
        print()
    except Exception as err:
        print(f"Error. Employee was not added ({err})")
    
    return None

def get_all_employees(session, list_projects=False):
    with session:
        query = select(Employee)
        result = session.scalars(query).all()   # .all() converts the result to a list
        # results_list = list(result)           # this is the same as above
        results_list = result
        
        print()
        if results_list:
            for person in results_list:
                print(person)
                if person.projects and list_projects:
                    print("     Participates in projects:")
                    for project in person.projects:
                        print(f"     {project}")
        else:
            print("No employees found.")

    return None

def update_employee(session):
    person_id = input("Enter employee id you want to update: ")
    try:
        with session:
 
            query = select(Employee).filter_by(id=person_id)
            person = session.execute(query).scalar_one()
            print()
            
            while True:
                print(person)
                confirm = input("Are you sure you want to update this employee? (y/n): ")
                if confirm.lower() == 'y':
                    
                    print()
                    print("Enter new data (press enter to keep old data)")
                    new_data = get_input_for_employee()
                    
                    # here we check if the new data is empty, if it is, we keep the old data
                    processed_data = [
                        new_data[i] if new_data[i] not in [None, ''] else getattr(person, attr)
                        for i, attr in enumerate(['name', 'last_name', 'dob', 'salary', 'position', 'unit_id'])
                    ]
                    
                    query = (
                        update(Employee)
                        .where(Employee.id == person_id)
                        .values(
                            name=processed_data[0],
                            last_name=processed_data[1], 
                            dob=processed_data[2], 
                            salary=processed_data[3], 
                            position=processed_data[4],
                            unit_id=processed_data[5])
                    )
                    session.execute(query)
                    session.commit()
                    
                    print("Employee updated")
                    break
                elif confirm.lower() == 'n':
                    print("Update aborted")
                    break
                else:
                    print("Invalid input")

            print()
            input("Press enter to continue...")
            print()
                
    except NoResultFound:
        print("Employee not found")
        print()
        input("Press enter to continue...")
    return None

def delete_employee(session):
    person_id = input("Enter employee id you want to delete: ")
    try:
        with session:  
            query = select(Employee).filter_by(id=person_id)
            person = session.execute(query).scalar_one()
            print()
            while True:
                print(person)
                confirm = input("Are you sure you want to delete this employee? (y/n): ")
                if confirm.lower() == 'y':
                    session.delete(person)
                    session.commit()
                    print("Employee deleted")
                    break
                elif confirm.lower() == 'n':
                    print("Delete aborted")
                    break
                else:
                    print("Invalid input")

            print()
            input("Press enter to continue...")
            print()
    except NoResultFound:
        print("Employee not found")
        print()
        input("Press enter to continue...")
    return None