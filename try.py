# Group Allocation Program using File Handling

# Ask user for group number
group = int(input("Enter your group number (1-7): "))

# Open and read the student file
file = open("students.txt", "r")

students = []

# Read each line from file
for line in file:
    data = line.strip().split(",")

    # Skip invalid lines
    if len(data) != 3:
        continue

    serial = data[0]
    name = data[1]
    student_id = data[2]

    # Get last digit of student ID
    last_digit = int(student_id[-1])

    # Conditions for each group
    if group == 1 and (last_digit == 2 or last_digit == 3):
        students.append([serial, name, student_id])

    elif group == 2 and (last_digit == 4 or last_digit == 5):
        students.append([serial, name, student_id])

    elif group == 3 and (last_digit == 6 or last_digit == 7):
        students.append([serial, name, student_id])

    elif group == 4 and (last_digit == 8 or last_digit == 9):
        students.append([serial, name, student_id])

    elif group == 5 and (last_digit == 0 or last_digit == 1):
        students.append([serial, name, student_id])

    elif group == 6 and int(student_id) % 2 == 0:
        students.append([serial, name, student_id])

    elif group == 7 and int(student_id) % 2 != 0:
        students.append([serial, name, student_id])

# Close the file
file.close()

# Sort students according to Student ID
students.sort(key=lambda x: int(x[2]))

# Display total students
print("\nTotal Students:", len(students))

# Display student names
print("\nSelected Students:")
for student in students:
    print(student[1])

# Display first and last student according to Student ID
if len(students) > 0:
    print("\nFirst Student:")
    print("Name:", students[0][1])
    print("Student ID:", students[0][2])

    print("\nLast Student:")
    print("Name:", students[-1][1])
    print("Student ID:", students[-1][2])

# Create output file
output_file = open("group_" + str(group) + ".txt", "w")

# Store processed student records
for student in students:
    output_file.write(student[0] + "," + student[1] + "," + student[2] + "\n")

# Close output file
output_file.close()

print("\nRecords saved successfully in group_" + str(group) + ".txt")