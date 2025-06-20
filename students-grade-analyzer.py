#Function that creates a student
def create_student(name,grade): 
    if grade.isdigit():
        grade = int(grade)
        if grade >=0 and grade <=100:
            return [name, grade]
        else: print("Grade must be between 1 and 100")
    else: print("enter a valid number")

student_number = input("How many students do you have? ")
if student_number.isdigit() and int(student_number) > 0:
    student_number=int(student_number)
    students = []
else:
    print("Enter a valid number")
    exit()

#Creating multiple students
for i in range(student_number):
    name = input("Name: ")
    grade = input("Grade: ")
    student = create_student(name,grade)
    students.append(student)

def display_student_summary(students):
    for student in students:
        name = student[0]
        grade = student[1]
        print(name, " has gotten ", grade)

# display_student_summary(students)