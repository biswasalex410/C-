class Student:
    roll = ""
    gpa = ""
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = Student(464,4.50)
rahim.display()

karim = Student(525,4.98)
karim.display()