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
#Step 1: Parse Header
#Use the names from the provided data: SL.No., Name, Std. Id
columns = [c.strip() for c in lines[0].strip().split('\t')]
#If your file uses commas instead of tabs, change .split('\t') to .split(',')

data_lines = lines[1:]

all_students = []
for line in data_lines:
    line = line.strip()
    if not line:
        continue
    #Splitting by tab as per your sample data layout
    values = [v.strip() for v in line.split('\t') if v.strip()]
    
    if len(values) >= 3:
        student = {
            'SL.No': values[0],
            'Name': values[1],
            'ID': values[2]
        }
        all_students.append(student)
        #Step 2: and now filter by ID ending in 4 and 5
group_2_students = [s for s in all_students if s['ID'].endswith('4') or s['ID'].endswith('5')]

#Step 3: Sort by ID 
group_2_sorted = sorted(group_2_students, key=lambda s: s['ID'])

#Step 4: Identify First and Last 
if group_2_sorted:
    first_student = group_2_sorted[0]
    last_student = group_2_sorted[-1]
else:
    print("No students found ending in 4 or 5.")
    exit()

#Step 5: Display and Save Results 
output_lines = []

def add_line(text):
    print(text)
    output_lines.append(text)