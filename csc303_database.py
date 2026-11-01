
import sqlite3

# Connect to the database
connection = sqlite3.connect("miva_university.db")

# Enable foreign key constraints
connection.execute("PRAGMA foreign_keys = ON")

# Create a cursor
cursor = connection.cursor()

# Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Student_ID TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Date_of_Birth TEXT NOT NULL
)
""")

# Create Instructor table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Instructor (
    Instructor_ID TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Phone_Number TEXT NOT NULL
)
""")

# Create Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    Course_Code TEXT PRIMARY KEY,
    Title TEXT NOT NULL,
    Credit_Hours INTEGER NOT NULL CHECK (Credit_Hours > 0),
    Department TEXT NOT NULL,
    Instructor_ID TEXT NOT NULL,
    FOREIGN KEY (Instructor_ID)
        REFERENCES Instructor(Instructor_ID)
)
""")

# Create Enrollment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    Student_ID TEXT,
    Course_Code TEXT,
    PRIMARY KEY (Student_ID, Course_Code),
    FOREIGN KEY (Student_ID)
        REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_Code)
        REFERENCES Course(Course_Code)
)
""")

# Save changes
connection.commit()

print("Database and four tables created successfully.")

# Verify the created tables
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name
""")

tables = cursor.fetchall()

print("\nTables in the database:")

for table in tables:
    print(table[0])


# Insert student records
students = [
    ("ST001", "Jeremiah Babatunde", "jeremiah001@example.com", "2002-04-12"),
    ("ST002", "Oluwatoyin Babatunde", "oluwatoyin002@example.com", "2001-08-20"),
    ("ST003", "Peter Musa", "peter003@example.com", "2003-01-15"),
    ("ST004", "Sarah Bello", "sarah004@example.com", "2002-11-09"),
    ("ST005", "Daniel Okoro", "daniel005@example.com", "2001-06-17"),
    ("ST006", "Grace Ade", "grace006@example.com", "2003-03-22"),
    ("ST007", "Michael Paul", "michael007@example.com", "2002-09-14"),
    ("ST008", "Esther John", "esther008@example.com", "2001-12-05"),
    ("ST009", "Samuel James", "samuel009@example.com", "2003-07-11"),
    ("ST010", "Faith Ibrahim", "faith010@example.com", "2002-02-18"),
    ("ST011", "David Peter", "david011@example.com", "2001-05-25"),
    ("ST012", "Ruth Daniel", "ruth012@example.com", "2003-10-08"),
    ("ST013", "Joseph Ade", "joseph013@example.com", "2002-01-30"),
    ("ST014", "Blessing Musa", "blessing014@example.com", "2001-09-19"),
    ("ST015", "Emmanuel Paul", "emmanuel015@example.com", "2003-06-13"),
    ("ST016", "Hannah Okoro", "hannah016@example.com", "2002-12-21"),
    ("ST017", "Isaac Bello", "isaac017@example.com", "2001-03-16"),
    ("ST018", "Deborah James", "deborah018@example.com", "2003-08-27"),
    ("ST019", "Joshua David", "joshua019@example.com", "2002-05-10"),
    ("ST020", "Elizabeth John", "elizabeth020@example.com", "2001-11-03")
]

cursor.executemany("""
INSERT OR IGNORE INTO Student
(Student_ID, Name, Email, Date_of_Birth)
VALUES (?, ?, ?, ?)
""", students)

print("Student records inserted successfully.")


# Insert instructor records
instructors = [
    ("INS001", "James Ade", "Computer Science", "08030000001"),
    ("INS002", "Mary Bello", "Mathematics", "08030000002"),
    ("INS003", "Peter Okoro", "Physics", "08030000003"),
    ("INS004", "Grace Musa", "Computer Science", "08030000004"),
    ("INS005", "David John", "Statistics", "08030000005"),
    ("INS006", "Sarah Paul", "Information Technology", "08030000006"),
    ("INS007", "Samuel Ade", "Mathematics", "08030000007"),
    ("INS008", "Ruth James", "Computer Science", "08030000008"),
    ("INS009", "Joseph Bello", "Physics", "08030000009"),
    ("INS010", "Esther Okoro", "Statistics", "08030000010"),
    ("INS011", "Daniel Musa", "Computer Science", "08030000011"),
    ("INS012", "Faith John", "Information Technology", "08030000012"),
    ("INS013", "Michael Paul", "Mathematics", "08030000013"),
    ("INS014", "Hannah Ade", "Computer Science", "08030000014"),
    ("INS015", "Isaac Bello", "Physics", "08030000015"),
    ("INS016", "Deborah James", "Statistics", "08030000016"),
    ("INS017", "Joshua Okoro", "Computer Science", "08030000017"),
    ("INS018", "Elizabeth Musa", "Information Technology", "08030000018"),
    ("INS019", "Emmanuel John", "Mathematics", "08030000019"),
    ("INS020", "Blessing Paul", "Computer Science", "08030000020")
]

cursor.executemany("""
INSERT OR IGNORE INTO Instructor
(Instructor_ID, Name, Department, Phone_Number)
VALUES (?, ?, ?, ?)
""", instructors)

print("Instructor records inserted successfully.")


# Insert course records
courses = [
    ("CSC101", "Introduction to Computer Science", 3, "Computer Science", "INS001"),
    ("CSC102", "Computer Programming", 3, "Computer Science", "INS004"),
    ("CSC201", "Data Structures", 3, "Computer Science", "INS008"),
    ("CSC202", "Database Systems", 3, "Computer Science", "INS011"),
    ("CSC301", "Software Engineering", 3, "Computer Science", "INS014"),
    ("CSC303", "Database Management", 3, "Computer Science", "INS017"),
    ("CSC305", "Computer Networks", 3, "Computer Science", "INS020"),
    ("MTH101", "General Mathematics", 2, "Mathematics", "INS002"),
    ("MTH102", "Calculus", 3, "Mathematics", "INS007"),
    ("MTH201", "Discrete Mathematics", 3, "Mathematics", "INS013"),
    ("PHY101", "General Physics", 3, "Physics", "INS003"),
    ("PHY102", "Applied Physics", 2, "Physics", "INS009"),
    ("PHY201", "Electronics", 3, "Physics", "INS015"),
    ("STA101", "Introduction to Statistics", 2, "Statistics", "INS005"),
    ("STA201", "Statistical Methods", 3, "Statistics", "INS010"),
    ("STA202", "Probability Theory", 3, "Statistics", "INS016"),
    ("ICT101", "Introduction to ICT", 2, "Information Technology", "INS006"),
    ("ICT201", "Web Development", 3, "Information Technology", "INS012"),
    ("ICT202", "Information Systems", 3, "Information Technology", "INS018"),
    ("ICT301", "Cybersecurity Fundamentals", 3, "Information Technology", "INS019")
]

cursor.executemany("""
INSERT OR IGNORE INTO Course
(Course_Code, Title, Credit_Hours, Department, Instructor_ID)
VALUES (?, ?, ?, ?, ?)
""", courses)

print("Course records inserted successfully.")


# Insert enrollment records
enrollments = [
    ("ST001", "CSC101"),
    ("ST001", "CSC202"),
    ("ST002", "CSC101"),
    ("ST002", "MTH101"),
    ("ST003", "CSC303"),
    ("ST003", "PHY101"),
    ("ST004", "CSC201"),
    ("ST004", "STA101"),
    ("ST005", "CSC102"),
    ("ST005", "ICT101"),
    ("ST006", "CSC305"),
    ("ST006", "MTH102"),
    ("ST007", "CSC202"),
    ("ST007", "ICT201"),
    ("ST008", "CSC301"),
    ("ST008", "STA201"),
    ("ST009", "CSC303"),
    ("ST009", "PHY201"),
    ("ST010", "ICT202"),
    ("ST010", "CSC101")
]

cursor.executemany("""
INSERT OR IGNORE INTO Enrollment
(Student_ID, Course_Code)
VALUES (?, ?)
""", enrollments)

print("Enrollment records inserted successfully.")


# Check the number of records in each table
print("\nDATABASE RECORD VERIFICATION")

table_names = ["Student", "Instructor", "Course", "Enrollment"]

for table in table_names:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    total = cursor.fetchone()[0]

    print(f"{table}: {total} records")


# Query A: List all students and their enrolled courses
print("\nSTUDENTS AND THEIR ENROLLED COURSES")

cursor.execute("""
SELECT Student.Name, Course.Title
FROM Student
LEFT JOIN Enrollment
ON Student.Student_ID = Enrollment.Student_ID
LEFT JOIN Course
ON Enrollment.Course_Code = Course.Course_Code
ORDER BY Student.Student_ID
""")

results = cursor.fetchall()

for row in results:
    print(row)


# Query B: Find the instructor teaching Database Systems
print("\nINSTRUCTOR TEACHING DATABASE SYSTEMS")

cursor.execute("""
SELECT Course.Title, Instructor.Name
FROM Course
JOIN Instructor
ON Course.Instructor_ID = Instructor.Instructor_ID
WHERE Course.Title = 'Database Systems'
""")

results = cursor.fetchall()

for row in results:
    print(row)



# Query C: Count students enrolled in each course
print("\nNUMBER OF STUDENTS ENROLLED IN EACH COURSE")

cursor.execute("""
SELECT Course.Title, COUNT(Enrollment.Student_ID)
FROM Course
LEFT JOIN Enrollment
ON Course.Course_Code = Enrollment.Course_Code
GROUP BY Course.Course_Code, Course.Title
ORDER BY Course.Course_Code
""")

results = cursor.fetchall()

for row in results:
    print(row)


# Close connection
connection.close()
