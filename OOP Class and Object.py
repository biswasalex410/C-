class Student:
    roll = " "
    gpa = " "

rahim = Student()
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.95
print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}")

karim = Student()
print(isinstance(karim,Student))
karim.roll = 102
karim.gpa = 4.85
print(f"Roll: {karim.roll}, GPA: {karim.gpa}")