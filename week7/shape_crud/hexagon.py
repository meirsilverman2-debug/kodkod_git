from calculator import Shape
from math import sqrt
# Level-6_Hexagon:

class Hexagon(Shape):
    def __init__(self, side):
        super().__init__(id, type)
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side ** 2) / 2
    
    def get_perimeter(self):
        return 6 * self.side
    
    def to_dict(self):
        return {"area": self.get_area(),"perimeter": self.get_perimeter()}


    def __str__(self):
        return f" The formula foe getting hexagon area is: (3 * 3 ** 0.5 * {self.side} ** 2) / 2 \n , and the formula for getting the perimeter is: 6 * {self.side}"


# h = Hexagon(2)

# print(h.get_area())
# print(h.get_perimter())
# print(h)
# print(h.to_dict())