# Lab03_02.py
# Purpose: Filter students whose IDs end with 4 or 5

output_filename = "group_2.txt" 

try:
    with open("student.txt", "r") as student_file:
        lines = student_file.readlines()
except FileNotFoundError:
    print("Error: 'student.txt' not found.")
    exit()

if not lines:
    print("Error: The file is empty.")
    exit()
