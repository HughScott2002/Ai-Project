# CRUD Operations for student_master
from controller.db_connect import *


# Create a student
def insert_student(
    studentID: int,
    studentName: str,
    studentEmail: str,
    studentProgramme: str,
    studentSchool: str,
):
    try:
        query = f"INSERT INTO student_master (student_Id, student_Name, student_email, school, programme) VALUES (%s, %s, %s, %s, %s)"
        values = (
            studentID,
            studentName,
            studentEmail,
            studentSchool,
            studentProgramme,
        )

        cursor.execute(query, values)
        conn.commit()

        print("Student successfully inserted.")
        return "Success"
    except Exception as e:
        print(f"Error inserting student: {e}")
        return "err"


# Retreves all the students
def retrieve_all_students():
    try:
        cursor.execute("SELECT * FROM student_master")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving all students: {e}")
        return "err"


# Retreves 1 the students
def retrieve_students(student_id: int):
    try:
        cursor.execute(f"SELECT * FROM student_master WHERE student_Id = {student_id}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving student: ID#{student_id}")
        print(f"Error : {e}")
        return "err"


# Updates a student
def update_student(
    studentID: int,
    studentName: str,
    studentEmail: str,
    studentProgramme: str,
    studentSchool: str,
):
    try:
        updateQuery = f"UPDATE student_master SET student_Name=%s, student_email=%s, school=%s, programme=%s WHERE student_Id=%s"
        updateValues = (
            studentName,
            studentEmail,
            studentSchool,
            studentProgramme,
            studentID,
        )
        cursor.execute(updateQuery, updateValues)
        conn.commit()
        print("Student Master Update Successfull")
        return "Success"
    except Exception as e:
        print(f"Error creating cursor: {e}")
        return "err"


# Delete a student
def delete_student(student_id):
    try:
        query = f"DELETE FROM student_master WHERE student_Id = %s"
        values = (student_id,)
        cursor.execute(query, values)
        conn.commit()

        print("Student successfully deleted.")
        return "Success"
    except Exception as e:
        print(f"Error deleting student: {e}")
        return "err"


# Delete a student
def delete_all_students():
    try:
        query = f"DELETE FROM student_master "
        cursor.execute(query)
        conn.commit()

        print("All Students successfully deleted.")
        return "Success"
    except Exception as e:
        print(f"Error deleting student: {e}")
        return "err"
