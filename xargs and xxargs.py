#xargs
"""
def student(id,name):
    print(id,name)
student(191,"Alex Biswas")
"""

"""
def student(*details):
    print(details)
student(191,"Alex",3.46)
student(192,"Alex",3.46)
"""

"""
def add(*numbers):
    sum = 0
    for num in numbers:
     sum = sum + num
    print(sum)
add(10,15)
add(10,15,20)
add(10,15,20,25)
"""
#xxagrs
def student(**details):
    print(details)

student(id=191,name="Alex")