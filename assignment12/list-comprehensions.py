# Task 3: List Comprehensions Practice
import pandas as pd

try:
    df = pd.read_csv('./csv/employees.csv')
    print("DataFrame successfully loaded:")
    print(df.head())

except FileNotFoundError:
    print(f"Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

employee_names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print(employee_names)

# Using a list comprehension, create another 
# list from the previous list of names. 
# This list should include only those names that contain the letter "e". Print this list.
employee_names_cont_e = [name for name in employee_names if "e" in name ]
print(employee_names_cont_e)