from controller.util.probation_reports import *

years = [
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
]
timer_seconds = 300

# When the function is done, start a new timer
# timer.start()


def run_all_probation_reports_for_everyone():
    # timer = threading.Timer(timer_seconds, run_all_probation_reports_for_everyone())
    # timer.start()
    for year in years:
        run_probation_reports(year)
    # When the function is done, start a new timer
    # timer = threading.Timer(timer_seconds, run_all_probation_reports_for_everyone)
    # timer.join()
    # timer.start()


# timer = threading.Timer(timer_seconds, run_all_probation_reports_for_everyone)
