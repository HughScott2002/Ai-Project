# CRUD Student Routes
from routes.database_routes.student_routes.routes import *
from routes.database_routes.module_details.routes import *
from routes.database_routes.module_master.routes import *
from routes.database_routes.probation_routes.routes import *
import random
import faker

fake = faker.Faker()


def seedDatabase():
    modules = [
        "CUS19",
        "ENG42",
        "MAT15",
        "PHY28",
        "CHE03",
        "BIO21",
        "HIS07",
        "GEO29",
        "ECO12",
        "ART36",
        "PSY50",
        "SOC18",
        "CSE10",
        "ECE25",
        "MEC33",
        "MUS14",
        "FRE27",
        "SPA04",
        "GER09",
        "ITA22",
        "JPN31",
        "CHI16",
        "RUS38",
        "ARF11",
        "PHI20",
        "POL44",
        "IND02",
        "KOR05",
        "THA30",
        "HIN13",
        "MAL35",
        "SWE08",
        "DUT49",
        "FIN26",
        "NOR48",
        "POR17",
        "TUR23",
        "VIK37",
        "SWA06",
        "ZUL40",
        "AFR32",
        "MNG45",
        "LAO21",
        "CAM14",
        "BEN03",
        "TAM09",
        "TEL12",
        "KAN25",
        "MAR18",
        "URD47",
    ]
    student_name = [fake.name() for _ in range(400)]
    programme_codes = [
        "SCIT",
        "BUSI",
        "ENGR",
        "ARCH",
        "HEAL",
        "ARTS",
        "LAW",
        "EDUC",
        "SCI",
        "MATH",
    ]
    delete_all_probations()
    delete_module_details_all()
    delete_all_modules()
    delete_all_students()
    for mod in modules:
        num_modules = random.randint(1, 4)
        insert_module(mod, num_modules)
    i = 0
    while i < 50:
        module: str = modules[random.randint(0, 49)]
        name: str = student_name[random.randint(0, 399)]
        email_name = name.replace(" ", "").lower()
        student_email = f"{email_name}@mail.com"
        student_school = "Utech"
        student_programme = programme_codes[random.randint(0, 8)]
        year_num = random.randint(2019, 2024)
        year: str = f"{year_num}"
        semester: int = random.randint(1, 2)
        student_id_concat = f"{year_num % 100}{random.randint(10001, 99991)}"
        student_id: int = int(student_id_concat)
        grade_points: float = round(random.uniform(1.1, 35.0), 2)
        print(
            module,
            year,
            semester,
            grade_points,
            student_id,
            name,
            student_email,
            student_school,
            student_programme,
        )
        i += 1
        insert_student(
            student_id, name, student_email, student_programme, student_school
        )
        # insert_addviser()

        for j in range(5):
            mod = modules[j]
            insert_module_detail(
                mod, year, 1, student_id, round(random.uniform(0.1, 3.0), 2)
            )
        for k in range(5):
            mody = modules[k + 5]
            insert_module_detail(
                mody, year, 2, student_id, round(random.uniform(0.1, 3.0), 2)
            )
    return "Success"


# works
# insert_student(student_id, name, student_email, student_programme, student_school)
# retrieve__module_details_with_year(2000)
# for i in 50:
# insert_module_detail(module, 2000, semester)
# cursor.close()
# conn.close()
