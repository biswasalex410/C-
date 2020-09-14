def isFirstLastsame(numl):
    print("Given List is ",numl)
    firstElement = numl[0]
    lastElement = numl[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False
numl = [10,15,12,17,19]
print("Result is ",isFirstLastsame(numl))