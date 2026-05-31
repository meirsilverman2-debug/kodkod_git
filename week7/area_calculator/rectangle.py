from calculator import Shape

# Level-2_Rectangle:

class Rectangle(Shape):


    def __init__(self, width, height):

        self.width = width
        self.heigth = height

    def get_area(self):
        if type(self.width) in [int, float] and self.width > 0 and type(self.heigth) in [int, type] and self.heigth > 0:
            return self.width * self.heigth
        
        print("All attr most be an int or flout not str and bigger than zero")
        return
        
    
    def get_perimeter(self):
        if type(self.width) in [int, float] and self.width > 0 and type(self.heigth) in [int, float] and self.heigth > 0:
            return (self.width + self.heigth) * 2
        
        print("All attr most be an int or flout not str and bigger than zero")
        return
    
    def to_dict(self):
        return {"area": self.get_area(),"perimeter": self.get_perimeter()}


    def __str__(self):
        if type(self.width) in [int, float] and self.width > 0 and type(self.heigth) in [int, float] and self.heigth > 0:
            return f" The formula for getting a rectangle perimter is: {self.width} + {self.heigth} * 2 = {(self.width + self.heigth) * 2}\n The formula for getting a rectangle area is:{self.width} * {self.heigth} = {(self.width + self.heigth)}"
        
        print("All attr most be an int or flout not str and bigger than zero")
        return
    

# r = Rectangle(2, 4)

# print(r.get_area())
# print(r.get_perimter())
# print(r)
# print(r.to_dict())