# hi

# IMPORTS - Valerie
from docx import Paragraph
from docx.shared import Pt

# OPTIONS AND INPUTS - Alvin
name = input("Enter your Name: ")
job_title = input("Enter your Job Title: ")
date = input("Enter todays Date (MM/DD/YYYY): ")
room_number = input("Enter your Room Number: ")

department = input("Select Department (1 = HR, 2 = IT, 3 = Finance): ")

if department == "1":
    department_name = "HR"
elif department == "2":
    department_name = "IT"
elif department == "3":
    department_name = "Finance"
else:
    raise ValueError("Invalid option. Please enter 1, 2, or 3.")
# WORD COMPONENTS - Arshia


# SAVING AND NAMING - Valerie
