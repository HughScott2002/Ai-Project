# CRUD Student Routes
from routes.database_routes.module_details.routes import *
from routes.database_routes.module_master.routes import *
import random

# import string


module: str = "TEST"
year: str = f"{random.randint(2019, 2024)}"
semester: int = random.randint(1, 3)
student_id: int = random.randint(1901041, 2401041)
grade_points: float = round(random.uniform(1.1, 35.0), 2)

print("Stuff Randomly Generated: \n")
print(module, year, semester, student_id, grade_points)

# Works
test1 = insert_module_detail(module, year, semester, student_id, grade_points)
if test1 == "Success":
    print("delete_module_details_for_student_and_module works\n")
# retrieve_all_module_details Works
test2 = retrieve_all_module_details()
if test2 != "err":
    print("delete_module_details_for_student_and_module works\n")
# retrieve_module_details_for_student works
test3 = retrieve_module_details_for_student(student_id)
if test3 != "err":
    print("delete_module_details_for_student_and_module works\n")

test4 = update_module_details_for_student(
    module, 2000, semester, student_id, grade_points
)
if test4 == "Success":
    print("update_module_details_for_student works\n")

print("After update\n")
retrieve_all_module_details()

test5 = delete_module_details_for_student_and_module(student_id, module)
if test5 == "Success":
    print("delete_module_details_for_student_and_module works\n")

cursor.close()
conn.close()
