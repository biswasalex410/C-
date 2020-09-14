#Map Function

def square(a):
    return a*a

num = [1,2,3,4,5]
result = list(map(square,num))
print(result)

# Filter function

num = [1,2,3,4,5]

result = list(filter(lambda x: x%2==0,num))
print(result)
