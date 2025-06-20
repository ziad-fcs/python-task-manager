student_number = input("How many students do you have? ")
if student_number.isdigit():
    student_number=int(student_number)
    students = []

else:
    print("Enter a valid number")
    exit()

name = input("Student name: ")
grade = input("Student grade: ")

#checking if grade is int & between 1 and 100
