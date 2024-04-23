# CRUD Operations for probation
from controller.db_connect import *


def insert_probation(
    student_id,
    student_name,
    semester1_gpa,
    semester2_gpa,
    cumlative_gpa,
    desired_gpa,
    year,
):
    try:
        query = f"INSERT INTO probation (student_id, student_name, semester1_gpa, semester2_gpa, cumlative_gpa, desired_gpa, year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (
            student_id,
            student_name,
            semester1_gpa,
            semester2_gpa,
            cumlative_gpa,
            desired_gpa,
            year,
        )
        cursor.execute(query, values)
        conn.commit()

        print("Probation successfully inserted.")
        return "Success"
    except Exception as e:
        print(f"Error inserting Probation: {e}")
        return "err"


# Retrieve all probation
def retrieve_all_reports():
    try:
        cursor.execute("SELECT * FROM probation")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving all probation: {e}")
        return "err"


# Retrieve a specific probation by ID
def retrieve_probation_by_student_id(student_id: int):
    try:
        cursor.execute(f"SELECT * FROM probation WHERE student_id = '{student_id}'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving probation: ID#{student_id}")
        print(f"Error: {e}")
        return "err"


# Retrieve a specific probation by year
def retrieve_probation_by_year(year: int):
    try:
        cursor.execute(f"SELECT * FROM probation WHERE year = '{year}'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving probation: {year}")
        print(f"Error: {e}")
        return "err"


# Update a probation
def update_probation(cumlative_gpa, desired_gpa, year, student_id):
    try:
        update_query = f"UPDATE probation SET cumlative_gpa = %s, desired_gpa = %s, year = %s WHERE student_id = %s"
        update_values = (cumlative_gpa, desired_gpa, year, student_id)

        cursor.execute(update_query, update_values)
        conn.commit()
        print("Probation Update Successful")
        return "Success"
    except Exception as e:
        print(f"Error updating probation: {e}")
        return "err"


# Delete a probation
def delete_probation(student_id: int):
    try:
        query = f"DELETE FROM probation WHERE student_id = %s"
        values = (student_id,)
        cursor.execute(query, values)
        conn.commit()

        print("Probation successfully deleted.")
        return "Success"

    except Exception as e:
        print(f"Error deleting probation: {e}")
        return "err"


def delete_all_probations():
    try:
        query = "DELETE FROM probation"
        cursor.execute(query)
        conn.commit()

        print("All Probation successfully deleted.")
        return "Success"

    except Exception as e:
        print(f"Error deleting probation: {e}")
        return "err"
