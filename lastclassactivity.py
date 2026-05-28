# Lab03_03.py
# Purpose: Read student IDs from students.txt
# Handles file errors and unexpected errors
print()
student_file = None

try:
    # Open the file
    student_file = open("student.txt", "r")

    # Read all lines
    lines = student_file.readlines()

    # Check if file is empty
    if not lines:
        print("Error: The file is empty.")
    else:
        print("Student IDs:")
        print("-" * 30)

        # Skip header line if needed
        for line in lines[1:]:
            line = line.strip()

            # Ignore blank lines
            if not line:
                continue

            # Split data by tab
            values = line.split('\t')

            # Print Student ID (3rd column)
            if len(values) >= 3:
                print(values[2])

except FileNotFoundError:
    print("Error: 'student.txt' does not exist.")

except Exception as e:
    print(f"Unexpected error occurred: {e}")

finally:
    # Close file if it was opened
    if student_file:
        student_file.close()

    # Completion message
    print("\nProgram execution completed.")
print()