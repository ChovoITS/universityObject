from student import Student
import sqlite3

def query(database, connection, query : str):
    
    queryOutput = database.execute(query)
    connection.commit()
    if queryOutput.fetchone() is not None:
        return queryOutput


def main():
    connection = sqlite3.connect("database/student.db")
    database = connection.cursor()
    result = query(database, connection, "SELECT * FROM student")
    studentList = []
    for row in result:
        studentList.append(Student(row[0], row[1], row[2], row[3]))
    studentBest = studentList[0]
    for student in studentList:
        if studentBest.getGPA() < student.getGPA():
            studentBest = student
    
    print(studentBest)

if __name__ == "__main__":
    main()