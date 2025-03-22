# Task 2: Read a CSV File
import csv
import os
import custom_module
from datetime import datetime

def read_employees():
    employees = {} #dictionary
    rows = [] #list
    firstRow = True
    try:
        with open('../csv/employees.csv', "r", newline='') as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                if firstRow: 
                    employees["fields"] = row # "fields":columns readers(firstRow)
                    firstRow=False  
                else:
                    rows.append(row)
            employees["rows"] = rows #dict employees: "rows":rows
        return employees   
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
    
employees = read_employees()

#Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)
    
employee_id_column=column_index("employee_id")
last_name_column=column_index("last_name")

# Task 4: Find the Employee First Name
def first_name(row_number):
    try:
        columnIndex = column_index("first_name")
        rows = employees["rows"]
        employee_row = rows[row_number]
        first_name = employee_row[columnIndex]
        return first_name
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id ):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort( key = lambda row: row[last_name_column])
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(employee_row):
    emp_keys = employees["fields"]
    emp_dict = dict([(k,v) for k,v in zip(emp_keys[1:],employee_row[1:])])
    return emp_dict
print (employee_dict(employees["rows"][2]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    list_employee_id = list(row[0] for row in employees["rows"])
    list_all_emp_dictionaries = []
    for employee_row in employees["rows"]:
        list_all_emp_dictionaries.append(employee_dict(employee_row))
    return dict([(k,v) for k,v in zip(list_employee_id, list_all_emp_dictionaries)])

print(f"All employee dictionaries: {all_employees_dict()}")

#  Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

#task 11:
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("lolo")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def get_dict_from_file(file_name):
        temp_dict = {}
        rows = [] #list
        firstRow = True
        try:
            with open(file_name, "r", newline='') as csvfile:
                data = csv.reader(csvfile)
                for row in data:
                    if firstRow: 
                        temp_dict["fields"] = row 
                        firstRow=False  
                    else:
                        rows.append(tuple(row) )
                temp_dict["rows"] = rows  
        except Exception as e:
            print(f"Exception type: {type(e).__name__}")
        return temp_dict 
# function that will use prev function just change the address
def read_minutes():
    minutes1 = get_dict_from_file('../csv/minutes1.csv')
    minutes2 = get_dict_from_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

# Task 13: Create minutes_set
def create_minutes_set():
   set_minutes1=set(minutes1["rows"])
   set_minutes2=set(minutes2["rows"])
   return set_minutes1.union(set_minutes2)

minutes_set = create_minutes_set()

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)    
    minutes_list = list(map(lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: (x[1]))
    print (f"The sorted minutes_list is:{minutes_list}")
    minutes_list_new_date_format = list(map(lambda row: (row[0], datetime.strftime(row[1], "%B %d, %Y")), minutes_list))
    print (f"The sorted minutes_list_new_date_format is:{minutes_list_new_date_format}")
    with open('./minutes.csv', "w") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in minutes_list_new_date_format:
            writer.writerow(row)    
    return minutes_list_new_date_format
write_sorted_list()