#understanding args
#takes unlimited positional arguements
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


# add(2,3,4,5)

#understanding kwargs
# takes an unlimited amount of key word arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n -= kwargs["subtract"]
    n /= kwargs["divide"]
    print(n)

# calculate(2, add=5, multiply=10, subtract=4, divide=2)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

car = Car(make="Nissan", model="X-Trail")
print(car.make)
print(car.model)

#the .get() helps create optional arguments that has not been initiated
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

car = Car(make="Nissan")
print(car.make)
print(car.model)# when we assign an attribute in the class with .get, then if the attribute is not specifed when initiating the class, then the call will return a None