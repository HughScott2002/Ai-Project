# CRUD Student Routes
from routes.database_routes.student_routes.routes import *
from routes.database_routes.module_details.routes import *
from routes.database_routes.module_master.routes import *
import random

# import string


module: str = "CUS18"
year: str = f"{random.randint(2019, 2024)}"
semester: int = random.randint(1, 3)
student_id: int = random.randint(1901041, 2401041)
grade_points: float = round(random.uniform(1.1, 35.0), 2)

print("Stuff Randomly Generated: ")
print(module, year, semester, student_id, grade_points)

# Works
insert_module_detail(module, year, semester, student_id, grade_points)

# retrieve_all_module_details Works
retrieve_all_module_details()

# retrieve_module_details_for_student works
retrieve_module_details_for_student(student_id)

test4 = update_module_details_for_student(
    module, 2000, semester, student_id, grade_points
)
if test4 == "Success":
    print("update_module_details_for_student works")

print("After update")
retrieve_all_module_details()
test5 = delete_module_details_for_student_and_module(student_id, module)
if test5 == "Success":
    print("delete_module_details_for_student_and_module works")

cursor.close()
conn.close()
