import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT
    )    
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses(
        courses_id INTEGER PRIMARY KEY,
        courses_name TEXT,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )    
''')

cursor.execute("INSERT INTO students (name) VALUES ('Festa')")
cursor.execute("INSERT INTO students (name) VALUES ('Sara')")

cursor.execute("INSERT INTO courses (courses_name, student_id) VALUES ('Math', 1)")
cursor.execute("INSERT INTO courses (courses_name, student_id) VALUES ('Science', 1)")
cursor.execute("INSERT INTO courses (courses_name, student_id) VALUES ('Art', 2)")

conn.commit()

cursor.execute('''
    SELECT students.name, courses.courses_name
    from students
    JOIN courses on students.student_id = courses.student_id
''')

rows = cursor.fetchall()
for row in rows:
    print(f"Students : {row[0]}, Course: {row[1]}")

conn.close()