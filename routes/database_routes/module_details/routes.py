# CRUD Operations for module_master
from controller.db_connect import *


# Create a module detail
def insert_module_detail(
    module: str,
    year: str,
    semester: int,
    student_id: int,
    grade_points: float,
):
    try:
        query = f"INSERT INTO module_details (module, year, semester, student_id, grade_points) VALUES (%s, %s, %s, %s, %s)"
        values = (module, year, semester, student_id, grade_points)

        cursor.execute(query, values)
        conn.commit()

        print("Module Detail successfully inserted.")
        return "Success"
    except Exception as e:
        print(f"Error inserting module detail: {e}")
        return "err"


# Retrieve all module details
def retrieve_all_module_details():
    try:
        cursor.execute("SELECT * FROM module_details")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving all module details: {e}")
        return "err"


# Retrieve all module details with year
def retrieve_module_details_with_year(selected_year):
    try:
        cursor.execute(f"SELECT * FROM module_details WHERE year = {selected_year}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving all module details: {e}")
        return "err"


# Retrieve module details for a specific student
def retrieve_module_details_for_student(student_id: int):
    try:
        cursor.execute(f"SELECT * FROM module_details WHERE student_id = {student_id}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving module details for student: ID#{student_id}")
        print(f"Error: {e}")
        return "err"


# Update module details for a specific student
def update_module_details_for_student(
    module: str,
    year: str,
    semester: int,
    student_id: int,
    grade_points: float,
):
    try:
        update_query = f"UPDATE module_details SET year = %s, semester = %s, grade_points = %s WHERE student_id = %s AND module = %s"
        update_values = (year, semester, grade_points, student_id, module)
        cursor.execute(update_query, update_values)
        conn.commit()
        print("Module Detail Update Successful")
        return "Success"
    except Exception as e:
        print(f"Error updating module detail: {e}")
        return "err"


# Delete module details for a specific student and module
def delete_module_details_for_student_and_module(student_id: int, module: str):
    try:
        query = f"DELETE FROM module_details WHERE student_id = %s AND module = %s"
        values = (student_id, module)
        cursor.execute(query, values)
        conn.commit()

        print("Module Detail successfully deleted.")
        return "Success"
    except Exception as e:
        print(f"Error deleting module detail: {e}")
        return "err"


# Delete module details for a specific student and module
def delete_module_details_all():
    try:
        query = f"DELETE FROM module_details"
        cursor.execute(query)
        conn.commit()

        print("All Module Details successfully deleted.")
        return "Success"
    except Exception as e:
        print(f"Error deleting module details: {e}")
        return "err"
