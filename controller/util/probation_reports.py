# from routes.database_routes.student_routes.routes import *
# from routes.database_routes.module_details.routes import *
# from routes.database_routes.module_master.routes import *
# from routes.database_routes.probation_routes.routes import *
from routes.prolog_routes.prolog import *
from routes.mail.routes import *
from databaseseeder import *

# from routes.prolog_routes.prolog import *
# import customtkinter as ctk
# import tkinter as tk
# from tkinter import messagebox, ttk
import threading


def run_probation_reports(YEAR: int, desired_GPA: float = 2.2):
    # get everything buy year
    desired_gpa = desired_GPA if desired_GPA else 2.2
    year_g = YEAR
    module_details = retrieve_module_details_with_year(year_g)
    # print(module_details)

    # Create a dictionary to store modules for each unique ID
    id_modules = {}

    # Iterate over module details
    for module in module_details:
        module_code = module[0]
        year = module[1]
        semester = module[2]
        id_number = module[3]
        score = module[4]
        module_master = retrieve_module_master_by_id(module_code)
        for item in module_master:
            credit = item[1]

        # Check if the ID is already in the dictionary
        if id_number in id_modules:
            id_modules[id_number]["modules"].append(module_code)
            id_modules[id_number]["scores"].append(score)
            id_modules[id_number]["semester"].append(semester)
            id_modules[id_number]["credit"].append(credit)
        else:
            # If not, create a new entry

            id_modules[id_number] = {
                "modules": [module_code],
                "scores": [score],
                "semester": [semester],
                "credit": [credit],
            }

    # Print the result
    for id_number, data in id_modules.items():
        modules = data["modules"]
        scores = data["scores"]
        semesters = data["semester"]
        credits = data["credit"]
        print(
            f"ID: {id_number}, Modules: {modules}, Scores: {scores}, Semester: {semesters}, Credit: {credits}"
        )
        # print("\n\n\n")
        # print(modules)
        # print(scores)
        # print(semesters)
        # print(credits)

    print(id_modules)

    for id_number, details in id_modules.items():
        modules = details["modules"]
        scores = details["scores"]
        semester = details["semester"]
        credit = details["credit"]
        student = retrieve_students(id_number)
        name = student[0][1] if student else " "
        student_email = student[0][2] if student else " "
        student_school = student[0][3] if student else " "
        # print(name_variable)
        # Call your calculate_gpa function
        gpas, cumulative_gpa = calculate_gpa(scores, credit, semester, modules)
        semester1_gpa = gpas[0] if gpas else 0
        semester2_gpa = gpas[1] if gpas else 0
        count = 30
        # Checking if the student already has a probation report
        oldRows = retrieve_probation_by_student_id(id_number)
        # If they do then, delete it
        if oldRows:
            # print("yes")
            for row in oldRows:
                (
                    student_id,
                    name,
                    value1,
                    value2,
                    value3,
                    value4,
                    year,
                    probation_id,
                ) = row
                print(student_id)
                delete_probation(student_id)
            # After it's deleted if they now fall under the treshold then add them back with the new desired GPA
            if round(cumulative_gpa, 2) <= desired_gpa:
                try:
                    insert_probation(
                        id_number,
                        name,
                        round(semester1_gpa, 2),
                        round(semester2_gpa, 2),
                        round(cumulative_gpa, 2),
                        desired_gpa,
                        year_g,
                    )
                except Exception as e:
                    print(f"Error occurred while inserting probation: {e}")
                try:
                    # student_email_scheduler = threading.Timer(
                    #     count,
                    #     student_mail(name, student_email, student_school, modules),
                    # )

                    # faculity_email_scheduler = threading.Timer(
                    #     count, faculity_mail(name, student_school, modules)
                    # )
                    # student_email_scheduler.start()
                    # faculity_email_scheduler.start()
                    student_mail(name, student_email, student_school, modules),
                    faculity_mail(name, student_school, modules)
                    count += 20
                except Exception as e:
                    print(f"Error occurred while scheduling emails: {e}")
                # time.sleep(2)

        else:
            if round(cumulative_gpa, 2) <= desired_gpa:
                try:
                    insert_probation(
                        id_number,
                        name,
                        round(semester1_gpa, 2),
                        round(semester2_gpa, 2),
                        round(cumulative_gpa, 2),
                        desired_gpa,
                        year_g,
                    )
                except Exception as e:
                    print(f"Error occurred while inserting probation: {e}")
                try:
                    #     student_email_scheduler = threading.Timer(
                    #         count,
                    #         student_mail(name, student_email, student_school, modules),
                    #     )

                    #     faculity_email_scheduler = threading.Timer(
                    #         count, faculity_mail(name, student_school, modules)
                    #     )
                    #     student_email_scheduler.start()
                    #     faculity_email_scheduler.start()
                    #     count += 20
                    student_mail(name, student_email, student_school, modules),
                    faculity_mail(name, student_school, modules)
                except Exception as e:
                    print(f"Error occurred while scheduling emails: {e}")
                # time.sleep(2)

    return "Success"
