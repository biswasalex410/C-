

n = int(input("Enter the last number: "))
sum = 0
for x in range(2,n+2,2):
    sum = sum+x*x
print(sum)