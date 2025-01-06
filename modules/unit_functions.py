# 1. Skyrių valdymas:
#    - Sukurkite galimybę pridėti/redaguoti įmonės skyrius (pavadinimas, vadovas, vieta)
#    - Kiekvienas darbuotojas priklauso vienam skyriui (One-to-Many ryšys)
#    - Galimybė peržiūrėti visus skyriaus darbuotojus
#    - Galimybė perkelti darbuotoją į kitą skyrių

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select, update
from models.unit import Unit
from models.employee import Employee

def get_input_for_new_unit():
    try:
        name = input("Enter unit name: ")
        head_id = input("Enter ID of the head of unit (press Enter if not known): ")
        if head_id == "":
            head_id = None  
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

def get_all_units(session):
    with session:
        query = select(Unit)
        result = session.scalars(query)
        results_list = list(result)
        print()
        print("-"*50)
        
        if results_list:
            for unit in results_list:
                print(unit)
                print("     Employees:")
                query2 = select(Employee).where(Employee.unit_id == unit.id)
                all_employees = session.scalars(query2)
                employees_list = list(all_employees)
                if employees_list:
                    for employee in employees_list:
                        print(f"     {employee}")
                else:
                    print("     No employees assigned to this unit.")
        else:
            print("No units found.")
                       
        print()
        input("Press enter to continue...")
        print()
    return None

def update_unit(session):
    unit_id = input("Enter unit id you want to update: ")
    try:
        with session:
 
            query = select(Unit).filter_by(id=unit_id)
            unit = session.execute(query).scalar_one()
            print()
            
            while True:
                print(unit)
                confirm = input("Are you sure you want to update this unit? (y/n): ")
                if confirm.lower() == 'y':
                    new_data = get_input_for_new_unit()

                    # here we check if the new data is empty, if it is, we keep the old data
                    processed_data = [
                        new_data[i] if new_data[i] not in [None, ''] else getattr(unit, attr)
                        for i, attr in enumerate(['name', 'head_id', 'location'])
                    ]

                    query = (
                        update(Unit)
                        .where(Unit.id == unit_id)
                        .values(
                            name=processed_data[0], 
                            head_id=processed_data[1], 
                            location=processed_data[2])
                    )
                    session.execute(query)
                    session.commit()
                    
                    print("Unit updated")
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
        print("Unit not found")
        print()
        input("Press enter to continue...")
    return None
