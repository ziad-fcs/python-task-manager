name = input("Student name: ")

grade = input("Student grade: ")

#checking if grade is int & between 1 and 100

if grade.isdigit():
    grade=int(grade)
    if grade>= 1 and grade<= 100:
        