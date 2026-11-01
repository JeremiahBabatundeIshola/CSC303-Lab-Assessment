
import sqlite3

# Connect to the database
connection = sqlite3.connect("employee_training.db")
cursor = connection.cursor()

# Enable foreign key enforcement
cursor.execute("PRAGMA foreign_keys = ON")

# Remove existing tables so the script can be run again
cursor.execute("DROP TABLE IF EXISTS Employee_Training")
cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute("DROP TABLE IF EXISTS Employee")

# 1. Create Employee table
cursor.execute("""
CREATE TABLE Employee (
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name TEXT NOT NULL,
    Department TEXT NOT NULL
)
""")

# 2. Create Course table
cursor.execute("""
CREATE TABLE Course (
    Course_Title TEXT PRIMARY KEY,
    Instructor TEXT NOT NULL
)
""")

# 3. Create Employee_Training table
cursor.execute("""
CREATE TABLE Employee_Training (
    Employee_ID INTEGER NOT NULL,
    Course_Title TEXT NOT NULL,
    Course_Date TEXT NOT NULL,
    Training_Location TEXT NOT NULL,

    PRIMARY KEY (Employee_ID, Course_Title),

    FOREIGN KEY (Employee_ID)
        REFERENCES Employee(Employee_ID),

    FOREIGN KEY (Course_Title)
        REFERENCES Course(Course_Title)
)
""")

# Insert employee records
employees = [
    (1001, "Alice Brown", "HR"),
    (1002, "Bob Miller", "IT"),
    (1003, "Charlie Reed", "Finance")
]

cursor.executemany("""
INSERT INTO Employee
(Employee_ID, Employee_Name, Department)
VALUES (?, ?, ?)
""", employees)

# Insert course records
courses = [
    ("Leadership", "Dr. Smith"),
    ("Conflict Resolution", "Dr. White"),
    ("Python Programming", "Prof. Green"),
    ("Data Security", "Dr. Black"),
    ("Financial Modeling", "Dr. Adams")
]

cursor.executemany("""
INSERT INTO Course (Course_Title, Instructor)
VALUES (?, ?)
""", courses)

# Insert employee training records
training_records = [
    (1001, "Leadership", "2024-03-10", "Online"),
    (1001, "Conflict Resolution", "2024-03-15",
     "Office Training Room"),
    (1002, "Python Programming", "2024-04-12", "Online"),
    (1002, "Data Security", "2024-04-15",
     "Office Training Room"),
    (1003, "Leadership", "2024-03-10", "Online"),
    (1003, "Financial Modeling", "2024-05-20",
     "Conference Hall"),
    (1003, "Python Programming", "2024-04-12", "Online")
]

cursor.executemany("""
INSERT INTO Employee_Training
(Employee_ID, Course_Title, Course_Date, Training_Location)
VALUES (?, ?, ?, ?)
""", training_records)

# Display the normalized training records
print("\nNORMALIZED EMPLOYEE TRAINING RECORDS")

cursor.execute("""
SELECT
    Employee.Employee_ID,
    Employee.Employee_Name,
    Employee.Department,
    Course.Course_Title,
    Course.Instructor,
    Employee_Training.Course_Date,
    Employee_Training.Training_Location
FROM Employee_Training
JOIN Employee
    ON Employee_Training.Employee_ID = Employee.Employee_ID
JOIN Course
    ON Employee_Training.Course_Title = Course.Course_Title
ORDER BY Employee.Employee_ID
""")

for record in cursor.fetchall():
    print(record)

# Verify the number of records in each table
print("\nTABLE RECORD VERIFICATION")

for table in ("Employee", "Course", "Employee_Training"):
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table}: {cursor.fetchone()[0]} records")

connection.commit()
connection.close()

print("\nDatabase implementation completed successfully.")
