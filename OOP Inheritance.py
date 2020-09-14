#Parents class , Super class, Base class
class Phone:
    def call(self):
        print("You can Call")

    def message(self):
        print("You can Message")

#Child class, Sub class, Derived class
class Samsung(Phone):
    def photo(self):
        print("You can Take Photo")

s = Samsung()
s.call()
s.message()
s.photo()

print(issubclass(Phone,Samsung))