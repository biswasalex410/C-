file = open("student.txt","r")
#print(file.readable())
#text = file.read()
#print(text)
#size = len(text)
#print(size)
#text = file.readlines()
for line in file:
    print(line)
#print(text)
file.close()