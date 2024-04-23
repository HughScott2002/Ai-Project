from routes.database_routes.student_routes.routes import *
from routes.database_routes.module_details.routes import *
from routes.database_routes.module_master.routes import *
from routes.database_routes.probation_routes.routes import *
from controller.util.probation_reports import *
from controller.util.run_for_all import *
from routes.prolog_routes.prolog import *
from routes.mail.routes import *
from databaseseeder import *
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from dotenv import load_dotenv
import os

# HUGH SCOTT
# ID# 1908850

# Load environment variables from .env file
load_dotenv()

# import threading
import schedule
import time

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
paths = os.getenv("PATH_TO_PROJECT_ASSETS_FRAME0")
ASSETS_PATH = OUTPUT_PATH / Path(rf"{paths}")

years = [
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
]
timer_seconds = 60


# TODO Fix the automatic runs
# When the function is done, start a new timer
schedule.every(5).minutes.do(run_all_probation_reports_for_everyone)


# Sumbit handler, gets the values from the GUI and
def submit():
    try:
        year = int(year_entry.get())
        desired_gpa = gpa_entry.get() if gpa_entry.get() else 2.2
        try:
            desired_gpa = float(desired_gpa)
            result = run_probation_reports(int(year), float(desired_gpa))
            if result == "Success":
                messagebox.showinfo("Success", "The operation was successful.")
                populate_table(year)
        except ValueError:
            return messagebox.showinfo("Invaild", "Please enter a valid GPA e.g")
    except ValueError:
        return messagebox.showinfo("Invaild", "Please enter a valid year")

    # result = run_probation_reports(int(year), float(desired_gpa))
    # if result == "Success":
    #     messagebox.showinfo("Success", "The operation was successful.")
    #     populate_table(year)


def populate_table(year: int):
    tree.delete(*tree.get_children())
    data = retrieve_probation_by_year(year)
    for i in data:
        tree.insert("", "end", values=i)


def initial_populate_table():
    tree.delete(*tree.get_children())
    data = []
    for year in years:
        data += retrieve_probation_by_year(year)
    for i in data:
        tree.insert("", "end", values=i)


def seeder_helper():
    tree.delete(*tree.get_children())
    seedDatabase()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x1080")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1080,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(247.0, 420.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(244.0, 314.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(350.0, 100.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(352.0, 114.0, image=image_image_4)

# entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(243.0, 312.0, image=entry_image_1)
year_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
year_entry.place(x=78.0, y=284.0, width=330.0, height=54.0)

# entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(248.0, 417.0, image=entry_image_2)
gpa_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
gpa_entry.place(x=83.0, y=389.0, width=330.0, height=54.0)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(90.0, 138.0, image=image_image_5)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
reesed_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=seeder_helper,
    relief="flat",
    bg="#FFFFFF",
)
reesed_button.place(x=522.0, y=388.0, width=125.0, height=52.5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(349.0, 51.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(650.0, 37.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(28.0, 28.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(363.0, 150.0, image=image_image_9)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
submit_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=submit,
    relief="flat",
    bg="#FFFFFF",
)
submit_button.place(x=505.0, y=277.0, width=160.0, height=62.0)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(383.0, 491.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(96.0, 259.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(126.0, 366.0, image=image_image_12)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(260.0, 491.0, image=image_image_13)
window.resizable(True, True)
# Create a Treeview widget
tree = ttk.Treeview(
    window,
    columns=(
        "Student_ID",
        "Student_Name",
        "Semester_1_GPA",
        "Semester_2_GPA",
        "Cumulative_GPA",
        "Desired_GPA",
        "Year",
        "Report_ID",
    ),
    show="headings",
)

# Add headings
tree.heading("Student_ID", text="Student ID")
tree.heading("Student_Name", text="Student Name")
tree.heading("Semester_1_GPA", text="Semester 1 GPA")
tree.heading("Semester_2_GPA", text="Semester 2 GPA")
tree.heading("Cumulative_GPA", text="Cumulative GPA")
tree.heading("Desired_GPA", text="Desired GPA")
tree.heading("Year", text="Year")
tree.heading("Report_ID", text="Report ID")
tree.place(x=0, y=524, height=566, width=700)
# Set up horizontal and vertical scrollbars
xscrollbar = ttk.Scrollbar(window, orient="horizontal", command=tree.xview)
yscrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)

tree.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
tree.place(x=0, y=524, height=566, width=700)
xscrollbar.place(x=0, y=1035, width=700)
yscrollbar.place(x=680, y=524, height=566)
initial_populate_table()
window.mainloop()
