from models.database import get_session
from modules.database_creator import create_all_tables
import modules.employee_functions as ef
import modules.unit_functions as uf

def main():
    db = get_session()

    while True:
        try:
            while True:
                
                selection = input(
                    f"Enter your action:\n"
                    f"EMPLOYEES:\n"
                    f"1. List all employees\n"
                    f"2. Add new person\n"
                    f"3. Update person\n"
                    f"4. Delete person\n"
                    f"---------------------\n"
                    f"UNITS:\n"
                    f"5. List all units\n"
                    f"6. Add new unit\n"
                    f"7. Update unit\n"
                    f"---------------------\n"
                    f"0. Exit\n"
                    f">> "
                )
                selection = int(selection)
                
                match selection:
                    case 1:
                        ef.get_all_employees(db)
                    case 2:
                        person = ef.get_input_for_employee()
                        ef.create_employee(person, db)
                    case 3:
                        ef.update_employee(db)
                    case 4:
                        ef.delete_employee(db)
                    case 5:
                        uf.get_all_units(db)
                    case 6:
                        unit = uf.get_input_for_new_unit()
                        uf.create_unit(unit, db)
                    case 7:
                        pass
                    case 0:
                        print()
                        print("Goodbye!")
                        print()
                        exit()
                    case _:
                        print ("Invalid input")
               
        except Exception as err:
            print(f"Error: {err}")
            input("Something went wrong. Try again. Press enter to continue...")
    

    # # task1.employee = new_employee
    # new_employee1.tasks.append(task1)
    # # new_employee.tasks.extend([task1, task2])

    # db.commit()

    # new_project1.employees.append(new_employee2)
    # new_project1.employees.append(new_employee1)

    # new_project2.employees.append(new_employee2)
    # new_project2.employees.append(new_employee1)
    # db.commit()

    # employee : Employee = db.query(Employee).get(2)

    # print("-"*50)
    # print(employee.name)

    # for project in employee.projects:
    #     print("     " + project.name)

    # print("-"*50)


if __name__ == "__main__":
    create_all_tables()
    main()