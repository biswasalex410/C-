def mergeList(list1, list2):
    print("First List ", list1)
    print("Second List ", list2)
    thirdList = []
    for num in list1:
        if (num % 2 != 0):
            thirdList.append(num)
    for num in list2:
        if (num % 2 == 0):
            thirdList.append(num)
    return thirdList
list1 = [10, 20, 35, 11, 27]
list2 = [13, 43, 33, 12, 24]

print("Result List is ", mergeList(list1, list2))