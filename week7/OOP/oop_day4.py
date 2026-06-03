# class A: pass

# class B(A): pass

# b = B()
# print(isinstance(b, A), isinstance(b, B))
# print(issubclass(B, A), issubclass(A, B))
# print(type(b) is B)
# print(type(b) is A)

# Excercises OOP Inheritance:
# exercise_1:

class Vehicle:
    def __init__(self):
        pass

    def open(self):
        print("The wehicle opened") 

class Car(Vehicle):
    def drive(self):
        print("The car is driving")

c = Car()
c.drive()
c.open()

# A car inherit from a vehicle because car is a type of vehicle.


# exercise_2: polymorphism

class Shape:
    def __init__(self):
        pass

    def area(self):
        return "area"


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


lst = [Shape(), Circle(4), Rectangle(2, 4)]

for inst in lst:

    # insted of doing this:
    if type(inst) == Shape:
        print("area")
    if type(inst) == Circle:
        print(inst.area())
    if type(inst) == Rectangle:
        print(inst.area())


    #in the right way of polymorphisem do this:
for inst in lst:

    print(inst.area())

# It does not break the main idea that the function calculat the aera we are changing only the implemntion of it depending on the shape.

class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()

print(type(my_dog)) # <class '__main__.Dog'>
print(isinstance(my_dog, Dog)) # True
print(isinstance(my_dog, Animal)) # True
print(issubclass(Dog, Animal)) # True
print(type(my_dog) == Animal) # False
if isinstance(my_dog, Animal):
    print("This object can be treated as an Animal.")


class Color:
    def __init__(self):
        pass

class Red(Color):
    def __init__(self):
        pass

class Yellow(Color):
    def __init__(self):
        pass

r = Red()

print(type(r) == Color) # output >> False
# because type on an object checks only the type of the object itself without checking is father class.

print(isinstance(r, Color)) # output >> True
# becaus isinstance is more flexable than type and it checks the father class as well.

