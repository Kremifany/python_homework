# Read data into a DataFrame, as described in the lesson.
# The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price
# from a JOIN of the line_items table and the product table. Hint: Your ON statement would be
# ON line_items.product_id = products.product_id.
import pandas as pd
import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    sql_statement = "SELECT li.line_item_id , li.quantity, p.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id "    
    df = pd.read_sql_query(sql_statement, conn)
    # Add a column to the DataFrame called "total". This is the quantity times the price. 
    df['total'] = df['quantity'] * df['price'] 
    print("total added")
    print(df.head())
    # Add groupby() code to group by the product_id.
    # Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'.
    # Print out the first 5 lines of the resulting DataFrame. Run the program to see if it is correct so far.
    df = df.groupby('product_id').agg({
    'line_item_id': 'count',  # Count occurrences for each product_id
    'total': 'sum',           # Sum the 'total' for each product_id
    'product_name': 'first'   # Take the first 'product_name' encountered for each product_id
})

    print(f"df grouped by product_id:\n {df.head()}")
    # Sort the DataFrame by the product_name column.
    df = df.sort_values('product_name')
    print(f"\nsorted by product_name df is:\n {df}","\n")

    df.to_csv("./order_summary.csv") 