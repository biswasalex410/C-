# Using string Function
"""
sampleStr = "Emma is good developer. Emma is a writer"
cnt = sampleStr.count("Emma")
print("Emma appeared",cnt,"times")
"""

#Without Using String function

def count_emma(str):
    print("Given String : ",str)
    count = 0
    for i in range(len(str) -1):
        count += str[i: i+4] == 'Emma'
    return count
count = count_emma("Emma is good devveloper. Emma is a writer")
print("Emma appeared ",count,"times")