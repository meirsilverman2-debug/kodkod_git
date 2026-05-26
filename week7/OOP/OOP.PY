# OOP Exercises:

# excercise_1:

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof"
    
dog = Dog("Manman")
print(dog.bark())

# excercise_2:

class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
    
    def area(self):
        return (self.width * self.hight) 

r = Rectangle(2, 4)
print(r.area())

# excercise_3:

class Counter:
    def __init__(self, count= 0):
        self.count = count
    
    def increment(self):
        self.count += 1
    
    def value(self):
        print(f"The amount is: {self.count}")
    
c = Counter()
c.increment()
c.increment()
c.value()

# excercise_4:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
p = Point(1, 2)
# Those are the same.
print(p)
print(p.__str__())

# excercise_5:

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        while self.balance > 0:
            self.balance -= amount

        print(f"You reached: {self.balance} so you cannot withdraw!!!")

b = BankAccount()
b.withdraw(100)
print(b.balance)

# excercise_6:

class Temperature:
    def __init__(self, celsius):
        self.value = celsius

    def celsius_to_fahrenheit(self):
        return self.value * 1.8 + 32

t = Temperature(20)
print(t.celsius_to_fahrenheit())

# excercise_7:

class Student:
    school = "Kodcode"
    def __init__(self, name):
        self.name = name

s1 = Student("Meir")

s2 = Student("Mimi")
s2.name = "Tzipi"

print(f"{s1.name} learns in: {s1.school}, {s2.name} doesn't learn in: {s2.school}")

# excercise_8:

class Playlist:
    count_instances = 0 
    def __init__(self):
        Playlist.count_instances += 1

    def __str__(self):
        return f"The amount of instances that were created {Playlist.count_instances}"
    
pl = Playlist()
pl2 = Playlist()

print(Playlist.count_instances)
print(pl)

# excercise_9:

class Money:
    def __init__(self, amount= 0):
        self.amount = amount
    
    def is_more_than(self, other):
        return self.amount > other
    
m = Money()
m1 = Money(10)
m2 = Money(-10)
print(m.is_more_than(m1.amount))
print(m.is_more_than(m2.amount))

# excercise_10:

class Playlist:
    def __init__(self):
        self.titles = []
    
    def provid(self, title):
        self.titles.append(title)
    
    def remove(self, title):
        self.titles.remove(title)
    
    def count_titles(self):
        count = 0
        for _ in self.titles:
           count += 1
        return f"This is the aqmount of titles in the playlist: {count}"
    
    def __str__(self):
        songs = " "
        for title in self.titles:
            songs += "  " + title
        return f"{songs} in your playlist"
        
    
playlist = Playlist()

playlist.provid("Michelle")
playlist.provid("Mom's hero")

playlist.remove("Mom's hero")

print(playlist.count_titles())
print(playlist)


# self study!! haaa
# class Meir:
#     def speak(self):
#         print("hii")

# m = Meir()
# m.speak()
# m.name = "Manman"

# print(m.name)