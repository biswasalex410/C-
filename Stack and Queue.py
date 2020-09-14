#Stack
"""
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)
books.pop()
print("Now the top book is :",books[-1])
print(books)
books.pop()
print("Now the top book is :",books[-1])
print(books)
books.pop()
if not books:
    print("No books left")

"""
#Queue
from collections import deque
bank = deque(["Alex","Sabuj","Sonia","Moeen"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
bank.popleft()
if not bank:
    print("no person left")