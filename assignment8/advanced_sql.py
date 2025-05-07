import datetime
import sqlite3
import traceback
        
#Task 1 
def total_price_of_five_first_orders():
    try:
        with  sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn: 
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()
            print(f"Successfully connected to 'lesson.db'")
            query = """SELECT o.order_id, SUM(li.quantity * p.price) 
                       FROM orders o JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id 
                       GROUP BY o.order_id ORDER BY o.order_id LIMIT 5;"""
            print("\nExecuting query to Find the total price of each of the first 5 orders...")
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#Task 2
def avg_customer_orders():
    try:
        with  sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn: 
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()
            print(f"Successfully connected to 'lesson.db'")
            print("\nFor each customer, find the average price of their orders\n")
            query = """SELECT c.customer_name, AVG(ot.total_price) AS average_total_price 
                    FROM customers c 
                    LEFT JOIN (SELECT o.customer_id AS customer_id_b, 
                                SUM(li.quantity * p.price) AS total_price
                                FROM orders o
                                JOIN line_items li ON o.order_id = li.order_id
                                JOIN products p ON li.product_id = p.product_id
                                GROUP BY o.order_id, o.customer_id) ot ON c.customer_id = ot.customer_id_b
                    GROUP BY c.customer_id, c.customer_name;"""
            print("\nExecuting query to find for each customer the average price of their orders...")
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Task 3
# Creates a new order for a specified customer with the 5 least expensive products.
# All database operations are performed within a single transaction.
def create_new_order():
    try:
        with  sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn: 
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()
            print(f"Successfully connected to 'lesson.db'")

 
            # --- Start Transaction ---
            conn.execute("BEGIN TRANSACTION")
            print("Transaction started.")

            # 1. Get customer_id
            cursor.execute("""SELECT customer_id FROM customers WHERE customer_name = ?""", ('Perez and Sons',))
            customer_result = cursor.fetchone()
            if not customer_result:
                print(f"Error: Customer 'Perez and Sons' not found.")
                conn.rollback() # Rollback if customer not found
                return
            customer_id = customer_result[0]
            print(f"Found customer_id: {customer_id} for 'Perez and Sons'")

            # 2. Get employee_id
            cursor.execute("""SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?""",('Miranda', 'Harris'))
            employee_result = cursor.fetchone()
            if not employee_result:
                    print(f"Error: Employee Miranda Harris not found.")
                    conn.rollback() # Rollback if employee not found
                    return
            employee_id = employee_result[0]
            print(f"Found employee_id: {employee_id} for Miranda Harris")


            # 3. Get the 5 least expensive products
            cursor.execute("""SELECT product_id FROM products ORDER BY price ASC LIMIT 5""")
            product_ids_results = cursor.fetchall()
            if not product_ids_results or len(product_ids_results) < 5:
                print(f"Error: Could not retrieve 5 least expensive products.")
                conn.rollback() # Rollback if products not found
                return
            product_ids = [row[0] for row in product_ids_results]
            print(f"Found {len(product_ids)} least expensive product_ids: {product_ids}")

            # 4. Create the order record
            current_date = datetime.date.today().isoformat()
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, ?)
                RETURNING order_id
            """, (customer_id, employee_id, current_date))
            new_order_id_result = cursor.fetchone()
            if not new_order_id_result:
                print("Error: Failed to create new order and retrieve order_id.")
                conn.rollback()
                return
            new_order_id = new_order_id_result[0]
            print(f"Created new order with order_id: {new_order_id}")

            # 5. Create the line_item records
            for product_id in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, ?)
                """, (new_order_id, product_id, 10))
                print(f"Added line item for product_id: {product_id}, quantity: 10 to order_id: {new_order_id}")

            # --- Commit Transaction ---
            conn.commit()
            print("Transaction committed successfully.")

            # 6. Verify and print the order details
            print("\n--- New Order Details ---")
            cursor.execute("""
                SELECT li.line_item_id, li.quantity, p.product_name, p.price
                FROM line_items li
                JOIN products p ON li.product_id = p.product_id
                WHERE li.order_id = ?
            """, (new_order_id,))

            order_items = cursor.fetchall()
            if order_items:
                total_order_cost = 0
                print(f"Order ID: {new_order_id}")
                print(f"Customer: 'Perez and Sons' (ID: {customer_id})")
                print(f"Processed by Employee ID: {employee_id}")
                print("Items:")
                for item in order_items:
                    line_item_id, quantity, product_name, price = item
                    item_total = quantity * price
                    total_order_cost += item_total
                    print(f"  - Line Item ID: {line_item_id}, Product: '{product_name}', Quantity: {quantity}, Unit Price: ${price:.2f}, Item Total: ${item_total:.2f}")
                print(f"Total Order Cost: ${total_order_cost:.2f}")
            else:
                print(f"No line items found for order_id: {new_order_id}. This might indicate an issue.")

    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
        if conn:
            print("Rolling back transaction due to error.")
            conn.rollback()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        if conn:
            print("Rolling back transaction due to unexpected error.")
            conn.rollback()
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")
# Task4
# SQL query to find employees with more than 5 orders
def get_employees_with_many_orders():

    try:
        # conn = sqlite3.connect('lesson.db')
        # cursor = conn.cursor()
        # print(f"Successfully connected to 'lesson.db'")

        with  sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn: 
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()
            print(f"Successfully connected to 'lesson.db'")
       
            query = """SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
                        FROM employees e
                        JOIN orders o ON e.employee_id = o.employee_id
                        GROUP BY e.employee_id
                        HAVING COUNT(o.order_id) > 5;"""

            print("\nExecuting query to find employees with more than 5 orders...")
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("\n--- Employees with More Than 5 Orders ---")
            
                for row in results:
                    employee_id, first_name, last_name, order_count = row
                    print(f"{employee_id} {first_name} {last_name} {order_count}")
            else:
                print("\nNo employees found with more than 5 orders.")

    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == '__main__':
    total_price_of_five_first_orders()
    avg_customer_orders()
    create_new_order()
    get_employees_with_many_orders()






