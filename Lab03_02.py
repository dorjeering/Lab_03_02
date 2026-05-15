file = open('students.txt', 'r')
lines = file.readlines()
file.close()
group = int(input("Enter your group number (1-7): "))
selected_students = []
for line in lines:
    line = line.strip()
    data = line.split(",")
    if len(data) < 3:
        continue
    serial = data[0]
    name = data[1]
    student_id = data[2]
    last_digit = int(student_id[-1])
    if group == 1 and (last_digit == 2 or last_digit == 3):
        selected_students.append((serial, name, student_id))
    elif group == 2 and (last_digit == 4 or last_digit == 5):
        selected_students.append((serial, name, student_id))
    elif group == 3 and (last_digit == 6 or last_digit == 7):
        selected_students.append((serial, name, student_id))
    elif group == 4 and (last_digit == 8 or last_digit == 9):
        selected_students.append((serial, name, student_id))
    elif group == 5 and (last_digit == 0 or last_digit == 1):
        selected_students.append((serial, name, student_id))
    elif group == 6 and (last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8):
        selected_students.append((serial, name, student_id))
    elif group == 7 and (last_digit == 1 or last_digit == 3 or last_digit == 5 or last_digit == 7 or last_digit == 9):
        selected_students.append((serial, name, student_id))
selected_students.sort()
print("\nSelected students:")
for student in selected_students:
    print(f"Name: {student[1]}, ID: {student[2]}")
print("\nTotal number of students: ", len(selected_students))
if len(selected_students) > 0:
    print("First student: ", selected_students[0][1], "-", selected_students[0][0])
    print("Last student: ", selected_students[-1][1], "-", selected_students[-1][0])
output_file = open("group_" + str(group) + ".txt", "w")
for student in selected_students:
    output_file.write(student[2] + "," + student[1] + "," + student[0] + "\n")
output_file.close()
print("\nData saved in group_" + str(group) + ".txt")