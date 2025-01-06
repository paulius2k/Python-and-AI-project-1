from datetime import datetime

def date_input(msg, allow_future=True):
    while True:
        try:
            date = datetime.strptime(input(f"{msg}"), "%Y-%m-%d")
            if not allow_future and date > datetime.now():
                raise ValueError
            break
        except ValueError:
            print("Invalid date format or date is in the future")
    return date
    