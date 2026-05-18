print()
group = int(input("Enter the group number (1-7): "))

output_filename = f"group_{group}.txt" 

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
    last_digit = int(student['ID'][-1])
    if group == 1 and (last_digit == 2 or last_digit == 3):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 2 and (last_digit == 4 or last_digit == 5):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 3 and (last_digit == 6 or last_digit == 7):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 4 and (last_digit == 8 or last_digit == 9):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 5 and (last_digit == 0 or last_digit == 1):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 6 and (int(student['ID']) % 2 == 0):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    elif group == 7 and (int(student['ID']) % 2 != 0):
        all_students.append([student['SL.No'], student['Name'], student['ID']])
    #Step 2: and now filter by ID ending digit for the selected group
    group_students = [s for s in all_students if student['ID'].endswith(str(last_digit)) or s['ID'].endswith(str(last_digit))]

    #Step 3: Sort by ID 
    group_sorted = sorted(group_students, key=lambda s: student['ID'])




    #Step 4: Identify First and Last 
    if group_sorted:
        first_student = group_sorted[0]
        last_student = group_sorted[-1]
    else:
        print(f"No students found in group {group}.")
        exit()

#Step 5: Display and Save Results 
    output_lines = []

    def add_line(text):
        print(text)
        output_lines.append(text)

    add_line("=" * 50)
    add_line(f"       STUDENTS IN GROUP {group}")
    add_line("=" * 50)
    add_line(f"\nTotal number of students found: {len(group_sorted)}\n")

    add_line("Names of selected students:")
    add_line("-" * 30)
for idx, student in enumerate(group_sorted, start=1):
    add_line(f"  {idx}. {student['Name']} (ID: {student['ID']})")

add_line("\n" + "-" * 50)
add_line("First Student (by ID):")
add_line(f"  ID   : {first_student['ID']}")
add_line(f"  Name : {first_student['Name']}")

add_line("\nLast Student (by ID):")
add_line(f"  ID   : {last_student['ID']}")
add_line(f"  Name : {last_student['Name']}")
add_line("=" * 50)

with open(output_filename, "w") as out_file:
    out_file.write("\n".join(output_lines))

print(f"\nSuccess! Results saved to '{output_filename}'.")