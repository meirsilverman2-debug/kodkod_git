from calculator import Shape
import math
# Level-5_Circle:

class Circle(Shape):
    def __init__(self, r):
        super().__init__(1, "circle")
        self.r = r

    def get_area(self):
        return  math.pi * (self.r ** 2)

    def to_dict(self):
        return {"area": round(self.get_area(), 2),"perimeter": round(self.get_perimeter(), 2)}


    def get_perimeter(self):
        return  (math.pi * self.r) * 2
    
    def __str__(self):
        return f"The formula for getting a circle area is: {math.pi} * {self.r * 2} * 2 = {math.pi * self.r } \n The formula for getting a circle perimeter is: ({math.pi} * {self.r}) * 2 = {(math.pi * self.r) * 2} "


# c = Circle(2)

# print(c.get_area())
# print(c.get_perimeter())
# print(c)
# print(c.to_dict())