def divisible(numl):
    print("Given List is ",numl)
    print("Divisible of 5 in a list ")
    for num in numl :
        if (num % 5 == 0):
            print(num)

numl = [10, 15, 12, 17, 20]
divisible(numl)