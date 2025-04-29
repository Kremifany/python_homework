import sqlite3 

try:
    with sqlite3.connect("./db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()
        # def add_publisher(cursor, name):
        #     print("Inside add_publisher")
        #     try:
        #         cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
        #     except sqlite3.IntegrityError:
        #         print(f"{name} is already in the database.")

        # add_publisher(cursor, "Condé Nast")
        # def add_magazine(cursor, name, publisher):
        #     cursor.execute("SELECT publisher_id FROM Publishers WHERE name = (?);", (publisher,))
        #     results = cursor.fetchall()
        #     if len(results) == 0:
        #         print("This publisher not excist in the DB ")
        #         return
        #     publisher_id = results[0][0]
        #     try:
        #         cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?);", (name,publisher_id))
        #     except sqlite3.IntegrityError:
        #         print(f"{name} is already in the database.")

        # def add_subscriber(cursor, name, address ):
        #         cursor.execute("SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ? AND subscriber_address = ?;", (name,address))
        #         results = cursor.fetchall()
        #         if len(results) > 0:
        #             print("This subscriber already in DB")
        #             return
        #         cursor.execute("INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?,?)", (name, address))

        # def add_subscriptions(cursor, magazine,subscriber,address,expiration_date):
        #     cursor.execute("SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ? AND subscriber_address = ?;", (subscriber,address))
        #     results = cursor.fetchall()
        #     if len(results) > 0:
        #         subscriber_id=results[0][0]
        #     else:
        #         print(f"There was no subscriber named {subscriber}.")

        #     cursor.execute("SELECT * FROM Magazines WHERE magazine_name = ?", (magazine,)) 
        #     results = cursor.fetchall()
        #     if len(results) > 0:
        #         magazine_id = results[0][0]
        #     else:
        #         print(f"There was no magazine named {magazine}.")

        #     cursor.execute("SELECT * FROM Subscriptions WHERE magazine_id = ? AND subscriber_id = ?", (magazine_id,subscriber_id)) 
        #     results = cursor.fetchall()
        #     if len(results) > 0:
        #         print("that subscription already in DB")
        #         return
        #     else:
        #         cursor.execute("INSERT INTO Subscriptions (magazine_id, subscriber_id,expiration_date) VALUES (?, ?, ?)", (magazine_id, subscriber_id,expiration_date))


        # # === Add Publishers ===
        # print("\n--- Adding Publishers ---")
        # publishers_to_add = ["Condé Nast", "Hearst Communications", "Dotdash Meredith", "Future plc"]
        # for pub in publishers_to_add:
        #     add_publisher(cursor, pub)

        # # === Add Subscribers ===
        # print("\n--- Adding Subscribers ---")
        # subscribers_to_add = [
        #     ("Alice Smith", "123 Main St, Anytown, USA"),
        #     ("Bob Johnson", "456 Oak Ave, Sometown, USA"),
        #     ("Charlie Brown", "789 Pine Ln, Villagetown, USA"),
        #     ("Diana Prince", "1 Wonder Way, Themyscira, USA")
        # ]
        # for name, address in subscribers_to_add:
        #     add_subscriber(cursor, name, address)

        # # === Add Magazines ===
        # print("\n--- Adding Magazines ---")
        # magazines_to_add = [
        #     ("Vogue", "Condé Nast"),
        #     ("Cosmopolitan", "Hearst Communications"),
        #     ("People", "Dotdash Meredith"),
        #     ("PC Gamer", "Future plc")
        # ]
        # for name, pub in magazines_to_add:
        #     add_magazine(cursor, name, pub)

        # # === Add Subscriptions ===
        # print("\n--- Adding Subscriptions ---")
       
        # subscriptions_to_add = [
        #     ("Vogue", "Alice Smith", "123 Main St, Anytown, USA", 'April 27, 2024'),
        #     ("Cosmopolitan", "Bob Johnson", "456 Oak Ave, Sometown, USA", 'April 27, 2023'),
        #     ("People", "Charlie Brown", "789 Pine Ln, Villagetown, USA", 'April 27, 2023'),
        #     ("PC Gamer", "Alice Smith", "123 Main St, Anytown, USA", 'April 27, 2023'),
        # ]
        # for mag_name, sub_name, sub_addr, exp_date in subscriptions_to_add:
        #     add_subscriptions(cursor, mag_name, sub_name, sub_addr, exp_date)

        # Write a query to retrieve all information from the subscribers table.
        cursor.execute("SELECT * FROM Subscribers ")
        results = cursor.fetchall()
        if len(results) > 0:
            print("\nAll Subscribers are:\n")     
            for row in results:
                print(row)
        else:
            print("no subscribers got fetched from DB")
        # Write a query to retrieve all magazines sorted by name.
        cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name ")
        if len(results) > 0:
            results = cursor.fetchall()
            print("\nMagazines ordered by name:\n")
            for row in results:
                print(row)
        else:
            print("no magazines got fetched from DB")
        # Write a query to find magazines for a particular publisher, one of the publishers you created.
        # This requires a JOIN.

        cursor.execute("SELECT * FROM Publishers p JOIN Magazines m on p.publisher_id = m.publisher_id WHERE p.name = 'Condé Nast'")
        if len(results) > 0:
            results = cursor.fetchall()
            print("\nMagazines for publisher 'Condé Nast' are :\n")
            for row in results:
                print(row)
        else:
            print("no magazines for that publiher")

        

       # Commit changes
        conn.commit()
        print("\nDatabase population complete. Changes committed.")
    









        # cursor.execute("""CREATE TABLE IF NOT EXISTS Publishers(
        #                 publisher_id INTEGER PRIMARY KEY,
        #                 name TEXT NOT NULL UNIQUE
        #                 )""")
        # cursor.execute("""CREATE TABLE IF NOT EXISTS Magazines(
        #                 magazine_id INTEGER PRIMARY KEY,
        #                 magazine_name TEXT NOT NULL UNIQUE,
        #                 publisher_id INTEGER,
        #                 FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)   
        #                 )""")
        # cursor.execute("""CREATE TABLE IF NOT EXISTS Subscribers(
        #                 subscriber_id INTEGER PRIMARY KEY,
        #                 subscriber_name TEXT NOT NULL,
        #                 subscriber_address TEXT NOT NULL)""")
        # cursor.execute("""CREATE TABLE IF NOT EXISTS Subscriptions(
        #                 subscribtion_id INTEGER PRIMARY KEY,
        #                 subscriber_id INTEGER,
        #                 magazine_id INTEGER,
        #                 expiration_date TEXT NOT NULL,
        #                 FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
        #                 FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id))""")
    
    print("Tables created successfully.")


except Exception as e:
    print(f"An exception occurred: {e}")
else:
    print("All SQL operations completed.")
    
