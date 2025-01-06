from datetime import datetime
from modules.utilities import date_input

def get_input_for_project():
    try:
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        dob = date_input("Enter date of birth (YYYY-MM-DD): ", allow_future=False)
        salary = int(input("Enter salary: "))
        position = input("Enter position: ")
    except Exception as err:       
        print("Invalid input")
        return None
    return name, last_name, dob, salary, position