# 1. Skyrių valdymas:
#    - Sukurkite galimybę pridėti/redaguoti įmonės skyrius (pavadinimas, vadovas, vieta)
#    - Kiekvienas darbuotojas priklauso vienam skyriui (One-to-Many ryšys)
#    - Galimybė peržiūrėti visus skyriaus darbuotojus
#    - Galimybė perkelti darbuotoją į kitą skyrių

from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select, update
from models.unit import Unit

def get_input_for_new_unit():
    try:
        name = input("Enter unit name: ")
        head_id = input("Enter ID of the head of unit (press Enter if not known): ")
        location = input("Enter unit location: ")
    except Exception as err:       
        print("Invalid input")
        return None
    return name, head_id, location


def create_unit(unit, session):
    try:
        if unit:
            new_unit = Unit(name=unit[0], head_id=unit[1], location=unit[2])
            with session:
                session.add(new_unit)
                session.commit()
        
        print("Unit added")
        print()
    except Exception as err:
        print(f"Error. Unit was not added ({err})")
    
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
                    new_data = get_input()
                    
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