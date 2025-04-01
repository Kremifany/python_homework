import os
import pandas as pd
# Task1
# mistake in the test: 'charlie' starts from small letter 's' but in the task we have to do dictionary with capital 'C' 
# task1_data_frame  = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
# 'Age': [25, 30, 35],
# 'City': ['New York', 'Los Angeles', 'Chicago']})
task1_data_frame = pd.DataFrame({   'Name': ['Alice', 'Bob', 'charlie'], 
                            'Age': [25, 30, 35], 
                            'City': ['New York', 'Los Angeles', 'Chicago']})
print(task1_data_frame) 

#Task1.2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

#Task1.3
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

print(task1_older)

#Task1.4-Write to CSV file
task1_older.to_csv("employees.csv", index=False)

#Task2.1-Read from CSV file
task2_employees = pd.read_csv("employees.csv") 
print(task2_employees)

#Task2.2 -read from json file
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

#Task2.3 - combine df's from csv and json
more_employees=pd.concat([task2_employees,json_employees],ignore_index=True)
print(more_employees)

#Task3.1
first_three = more_employees.head(3)
print(first_three)

#Task3.2
last_two=more_employees.tail(2)
print(last_two)

#Task3.3
employee_shape = more_employees.shape
print(employee_shape)

#Task3.4
print(more_employees.info())

#Task4.1
from io import StringIO
dirty_data = pd.read_csv("dirty_data.csv")
clean_data = dirty_data.copy()

# Task4.2 -Remove any duplicate rows from the DataFrame
clean_data.drop_duplicates(inplace=True)
print(clean_data)

#Task4.3-Convert age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data)

#Task4.4-Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print(clean_data)

#Task4.5-Fill missing numeric values (use fillna).
#       -Fill Age which the mean and Salary with the median
median_salary = clean_data["Salary"].median()  # ignoring NaNs
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
mean_age = clean_data["Age"].mean()  # ignoring NaNs
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
print(clean_data)

#Task4.6-Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

#Task4.7-Strip extra whitespace and standardize Name and Department as uppercase
cols_to_clean = ['Name', 'Department']
for col in cols_to_clean:
    clean_data[col] = clean_data[col].str.strip().str.upper()
print(clean_data)