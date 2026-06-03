# OOP Exercise

# excercise_1:

class Dog:
    tail = True

    def __init__(self, breed, color, age, name= "Dog", sight="see" ):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.sight = sight

    def bark(self):
        return f"{self.name} say woof"
    
    def sleep(self):
        print(f"{self.name} is slepping shhhhhh!!!")
    
    def eat(self, food):
        return f" {self.name} is eatting {food} so yammy I think"
    
    def __str__(self):
        return f" {d.__dict__}"

d = Dog("I dont know", "brown", 12, "dawn")
print(d)
print(d.bark())

# excercise_2:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"width: {self.width} height: {self.height} rectangle-area: {self.width * self.height} "
    
    def __str__(self):
        return f"The area of this rectangle is: {self.width * self.height}"
    
r = Rectangle(2, 2)
print(r.area())
print(r.__dict__)
print(r)

# excercise_3:

class Counter:
    def __init__(self,amount= 0):
        self.amount = amount
    
    def increment(self):
        self.amount += 1
    
    def value(self):
        return f" The amount at the moment is: {self.amount}"
    
c = Counter(200)
c.increment()
c.increment()
c.increment()

print(c.value())
