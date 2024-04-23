# CRUD Student Routes
from routes.database_routes.student_routes.routes import *
from routes.database_routes.module_details.routes import *
from routes.database_routes.module_master.routes import *
import random

# import string


module: str = "CUS19"
student_name = ["Niran", "Gary", "Squidy", "Sheffy", "Quassip"]
student_email = "test@mail.com"
student_school = "Utech"
student_programme = "SCIT"
year: str = f"{random.randint(2019, 2024)}"
semester: int = random.randint(1, 3)
student_id: int = random.randint(1901041, 2401041)
grade_points: float = round(random.uniform(1.1, 35.0), 2)


# works
test_insert_student = insert_student(
    student_id,
    student_name[random.randint(0, 4)],
    student_email,
    student_school,
    student_programme,
)
if test_insert_student == "Success":
    print("test_insert_student works")

# works
test_retrieve_all_students = retrieve_all_students()
if test_retrieve_all_students != "err":
    print("test_retrieve_all_students works")
# works
test_retrieve_students = retrieve_students(student_id)
if test_retrieve_students != "err":
    print("test_retrieve_students works")
# works
test_update_student = update_student(
    student_id,
    student_name[random.randint(0, 4)],
    student_email,
    student_school,
    student_programme,
)
if test_update_student == "Success":
    print("test_update_student works")
cursor.close()
conn.close()
