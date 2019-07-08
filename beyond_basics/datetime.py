import datetime as dt
from dateutil.relativedelta import relativedelta

dob = input("Enter your date of birth('dd-mm-yyyy'): ")

def calculate_age(x):
    now = dt.datetime.now()
    birthdate =  dt.datetime.strptime(dob, '%d-%m-%Y')
    rdelta = relativedelta(now, birthdate) 
    return rdelta.years
    
y = calculate_age(dob)
print(y)
