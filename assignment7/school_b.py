import sqlite3 

# Connect to the database
with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # # Insert sample data into tables
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 

    # conn.commit() 
    # # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    # print("Sample data inserted successfully.")
    def add_student(cursor, name, age, major):
        try:
            cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    def add_course(cursor, name, instructor):
        try:
            cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")

    cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    def enroll_student(cursor, student, course):
        cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
        results = cursor.fetchall()
        if len(results) > 0:
            student_id = results[0][0]
        else:
            print(f"There was no student named {student}.")
            return
        cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
        results = cursor.fetchall()
        if len(results) > 0:
            course_id = results[0][0]
        else:
            print(f"There was no course named {course}.")
            return
        cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"Student {student} is already enrolled in course {course}.")
            return  
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

        # And at the bottom of your "with" block
    
    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")
    conn.commit() 
    # more writes, so we have to commit to make them final!
    cursor.execute ("SELECT * FROM Courses WHERE course_name LIKE 'math%'")
    results = cursor.fetchall()
    if len(results) > 0:
        print(results)
    else:
        print("no results")

    cursor.execute ("SELECT s.name, c.course_name FROM Students s JOIN Enrollments e ON s.student_id = e.student_id JOIN Courses c ON e.course_id = c.course_id")    
    results = cursor.fetchall()
    if len(results) > 0:
        print(results)
    else:
        print("no results")

    cursor.execute ("SELECT s.name, c.course_name FROM Enrollments e JOIN Students s ON e.student_id = s.student_id JOIN Courses c ON e.course_id = c.course_id")    
    results = cursor.fetchall()
    if len(results) > 0:
        print("second join\n")
        print(results)
    else:
        print("no results")


    cursor.execute ("UPDATE Students SET name='Charles', age=20 WHERE name='Charlie'")
    




