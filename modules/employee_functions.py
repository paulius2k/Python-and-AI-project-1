from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select, update
from models.employee import Employee
# from models.project import Project
# from models.task import Task
from models.database import get_session
from modules.utilities import date_input


def get_input_for_employee():
    try:
        name = input("Enter employee name: ")
        last_name = input("Enter employee last name: ")
        dob = date_input("Enter date of birth (YYYY-MM-DD): ", allow_future=False)
        salary = int(input("Enter salary: "))
        position = input("Enter employee position: ")
        unit = input("Enter employee's unit ID (press enter if not known): ")
    except Exception as err:       
        print("Invalid input")
        return None
    return name, last_name, dob, salary, position, unit


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

def get_all_employees(session):
    with session:
        query = select(Employee)
        result = session.scalars(query)
        print()
        for person in result:
            print(person)

        input("Press enter to continue...")
        print()
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
                    new_data = get_input_for_employee()
                    
                    query = (
                        update(Employee)
                        .where(Employee.id == person_id)
                        .values(
                            name=new_data[0], 
                            last_name=new_data[1], 
                            dob=new_data[2], 
                            salary=new_data[3], 
                            position=new_data[4])
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