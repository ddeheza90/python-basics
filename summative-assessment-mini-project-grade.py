# Define the function to convert a numeric score to a letter grade 

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
# Define a function to print all student summaries

def print_summary(student_list):
    print("\nStudent Summary:")
    for student in student_list: 
        name, score, grade = student 
        print(f"{name}: {score} -> {grade}")


# Starting to put things together

print("Welcome to the Student Grade Tracker!")

students = []  # This would be a list to store student data

add_more = "yes"

while add_more.lower() == "yes":
    name = input("Enter student name: ").title()    # Capitilizes each word in the name
    score = float(input("Enter score (0-100): "))   # Convert input to float 

    grade = get_letter_grade(score)                 # Call function to get letter grade
    students.append((name, score, grade))
    
    add_more = input("Add another student? (yes/no): ")

# Was not aware that I had to define the function to save student data to a file

def save_to_file(student_list):
    with open("grades.txt", "w") as file:
        for student in student_list:
            name, score, grade = student
            file.write(f"{name}: {score} -> {grade}\n")

# Show the the outsome and save to file

print_summary(students)                         # show student name, score, and grades
save_to_file(students)                          # Save the info to 'grades.txt
print("Student data saved to grades.txt")       # Thi will ensure that the data is saved