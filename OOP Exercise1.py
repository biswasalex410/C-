class Trinangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print(f"Base: {self.base}, Height: {self.height}","Area = ",area)

t1 = Trinangle(10,20)
t1.calculate_area()
t2 = Trinangle(20,30)
t2.calculate_area()