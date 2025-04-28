# import pandas as pd
# import sqlalchemy as sa
# import sqlite3
# import os
# db_path = "./db/lesson.db"

# if os.path.exists(db_path):
#     answer = input("The database exists.  Do you want to recreate it (y/n)?")
#     if answer.lower() != 'y':
#         exit(0)
#     os.remove(db_path)

# with sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn:    
#     conn = sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE')
#     conn.execute("PRAGMA foreign_keys = 1")
#     cursor = conn.cursor()
#     # customer_name,contact,street,city,country,postal_code,phone
#     # Create tables
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS customers (
#         customer_id INTEGER PRIMARY KEY,          
#         customer_name TEXT,
#         contact TEXT,
#         street TEXT,
#         city TEXT,
#         postal_code TEXT,
#         country TEXT,
#         phone TEXT
#     )
#     """)
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS employees (
#         employee_id INTEGER PRIMARY KEY,
#         first_name TEXT,
#         last_name TEXT,
#         phone TEXT      
#     )
#     """)
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS products (
#         product_id INTEGER PRIMARY KEY,
#         product_name TEXT,
#         price REAL
#     )
#     """)
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS line_items (
#         line_item_id INTEGER PRIMARY KEY,
#         order_id INTEGER,
#         product_id INTEGER,
#         quantity INTEGER,
#         FOREIGN KEY(order_id) REFERENCES orders(order_id),
#         FOREIGN KEY(product_id) REFERENCES products(product_id)
#     )
#     """)
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS orders (
#         order_id INTEGER PRIMARY KEY,
#         customer_id INTEGER,
#         employee_id INTEGER,
#         date TEXT,
#         FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
#         FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
#     )
#     """)
 
# # Create a database engine
# engine = sa.create_engine('sqlite:///db/lesson.db')

# tables = ["customers", "employees", 
#           "products", "orders", "line_items"]

# for table in tables:
#     t_name = table.lower()
#     csv_file = "./csv/" + table + ".csv"
#     data = pd.read_csv(csv_file, sep=',')
#     data.to_sql(t_name, engine, if_exists='append', index=False)

import pandas as pd
import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)