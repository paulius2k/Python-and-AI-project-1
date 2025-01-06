from datetime import datetime

def date_input(msg, allow_future=True):
    while True:
        try:
            err_msg = "Invalid date format"
            date = input(f"{msg}")
            if date in [None, '']:
                return ''
            else:
                date = datetime.strptime(date, "%Y-%m-%d")
                
            if not allow_future and date > datetime.now():
                err_msg = "Date is in the future"
                raise ValueError
            break
        except ValueError:
            print(f"{err_msg}")
            
    return date

def int_input(msg):
    while True:
        try:
            err_msg = "Invalid number format"
            num_str = input(f"{msg}")
            if num_str in [None, '']:
                return None
            else:
                num = int(num_str)
            break
        except ValueError:
            print(f"{err_msg}")
            
    return num