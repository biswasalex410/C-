#Regular method
"""
a = 20
b = 15
print("a = ",a)
print("b = ",b)
temp = a #temp = 20
a = b #a = 15
b = temp # b = 15

print("After Swapping")
print("a = ",a)
print("b = ",b)
"""
#Python Special Method
a = 20
b = 15
print("a = ",a)
print("b = ",b)
a, b = b, a
print("After Swapping")
print("a = ",a)
print("b = ",b)