from pyswip import Prolog


def calculate_gpa(grades, credits, semesters, modules):
    prolog = Prolog()
    prolog.consult(
        "d:/Documents/2023 Utech/AI/Project/projectprolog.pl"
    )  # Path to your Prolog file

    for i in range(len(grades)):
        prolog.assertz(
            "grade({}, semester{}, {})".format(modules[i], semesters[i], grades[i])
        )
        prolog.assertz("credit(module{}, {})".format(i + 1, credits[i]))

    gpas = []
    for semester in set(semesters):
        gpa_result = list(
            prolog.query("gpa(semester{}, GPA)".format(semester))
        )  # Query the GPA for each semester
        gpa = gpa_result[0]["GPA"] if gpa_result else None
        gpas.append(gpa)
        print("GPA for semester {}: {}".format(semester, gpa))

    cumulative_gpa_result = list(
        prolog.query(
            "cumulative_gpa(semester1, semester{}, CumulativeGPA)".format(
                max(semesters)
            )
        )
    )  # Query the cumulative GPA for all semesters
    cumulative_gpa = (
        cumulative_gpa_result[0]["CumulativeGPA"] if cumulative_gpa_result else None
    )
    print(
        "Cumulative GPA for semester 1 to semester {}: {}".format(
            max(semesters), cumulative_gpa
        )
    )

    return gpas, cumulative_gpa
