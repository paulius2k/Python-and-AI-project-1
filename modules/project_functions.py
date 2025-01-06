# 2. Projektų valdymas:
#    - Sukurkite projektų sistemą (pavadinimas, pradžios data, pabaigos data, statusas)
#    - Darbuotojai gali dirbti keliuose projektuose vienu metu (Many-to-Many ryšys)
#    - Galimybė priskirti/pašalinti darbuotojus iš projektų
#    - Galimybė peržiūrėti:
#      * Visus projekto darbuotojus
#      * Visus darbuotojo projektus

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select
from modules.utilities import date_input, int_input
from models.project import Project
from models.unit import Unit
from models.employee import Employee
import modules.employee_functions as ef

def get_input_for_new_project():
    try:
        name = input("Enter project name: ")
        start_dt = date_input("Enter project start date (YYYY-MM-DD): ", allow_future=True)
        end_dt = date_input("Enter project end date (YYYY-MM-DD): ", allow_future=True)
        status = input("Enter status: ")
    except Exception as err:       
        print("Invalid input")
        return None
    return name, start_dt, end_dt, status

def create_project(project, session):
    try:
        if project:
            new_project = Project(name=project[0], start_dt=project[1], end_dt=project[2], status=project[3])
            with session:
                session.add(new_project)
                session.commit()
        
        print("Project added")
        print()
    except Exception as err:
        print(f"Error. Project was not added ({err})")
        
def get_projects(session, project_id=None, list_employees=False):
    with session:
        query = select(Project)
        result = session.scalars(query)
        results_list = list(result)
        print()
        print("-"*50)
        
        if results_list:
            for project in results_list:
                if project.id == project_id or not project_id:
                    print(project)
                    if list_employees:
                        query2 = select(Employee).where(Employee.projects.any(Project.id == project.id))
                        all_employees = session.scalars(query2)
                        employees_list = list(all_employees)
                        if employees_list:
                            print("     Assigned employees:")
                            for employee in employees_list:
                                print(f"     {employee}")
                        else:
                            print("     No employees assigned to this project.")
        else:
            print("No projects found.")
                       
    return None

def modify_team_members(session, action):
    project_id = int_input("Enter project id you want to modify: ")
    try:
        with session:
 
            query_proj = select(Project).filter_by(id=project_id)
            project = session.execute(query_proj).scalar_one()
            
            while True:
                get_projects(session, project_id=project.id, list_employees=True)
                print()
                confirm = input("Are you sure you want to modify this project? (y/n): ")
                if confirm.lower() == 'y':
                    match action:
                        case "add":
                            ef.get_all_employees(session)
                            employee_id = int_input("Enter employee id you want to assign to this project: ")
                            query_empl = select(Employee).filter_by(id=employee_id)
                            employee = session.execute(query_empl).scalar_one()
                            
                            project:Project = session.execute(query_proj).scalar_one()
                            project.employees.append(employee)
                            session.commit()
                            print("Employee assigned")
                        case "remove":
                            employee_id = int_input("Enter employee id you want to remove from this project: ")
                            query_empl = select(Employee).filter_by(id=employee_id)
                            employee = session.execute(query_empl).scalar_one()
                            
                            project:Project = session.execute(query_proj).scalar_one()
                            project.employees.remove(employee)
                            session.commit()
                            print("Employee removed")
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
        print("Project not found")
        print()
        input("Press enter to continue...")
    return None