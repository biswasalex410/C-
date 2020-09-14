
def char(str):
    for i in range(0, len(str), 1):
        print("index[",i,"]", str[i])
str = input("Enter any name: ")

print("Print Single Charecter: ")
char(str)

"""

def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "pynative"
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)

"""