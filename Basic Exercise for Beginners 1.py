def multiplication_or_sum(num1,num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

num1 = int(input("Enter 1st integer number: "))
num2 = int(input("Enter 2nd integer number: "))
print("\n")
result = multiplication_or_sum(num1, num2)
print("The result is ", result)
