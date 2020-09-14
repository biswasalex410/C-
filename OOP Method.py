class Student:
    roll = ""
    gpa = ""
    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = Student()
rahim.set_value(464,3.98)
rahim.display()

karim = Student()
karim.set_value(525,4.98)
karim.display()